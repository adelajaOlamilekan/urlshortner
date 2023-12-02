from fastapi import(
    Depends,
    HTTPException,
    APIRouter,
    Request,
)
from fastapi.responses import RedirectResponse

from typing import Optional

from app.models.url_model import(
    URL_INFO
)

from app.settings import(
    API_BASE_URL, LINK_SHORTENER_ENCODING_SCHEME
)

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db_session


import hashlib
import argparse

router = APIRouter()

@router.post("/shorten-url/")
async def shorten_url(
        original_url: str, custom_back_half: str = None,
        db: Session = Depends(get_db_session),
):
    """
    Shortens the original link

    Args:
        original_link(str): The original link that is to be shortened.
        custom_back_half(str, Optional): An optional alternative custom name to replace the original link 
        db(Session, Optional): The db session.
    
    Returns:
        {
            "key": hash of long url, "original_url": original_url, 
            "shortened_url": shortened_url, "status_code" response code
        }

    """
    
    try:
        #check if original url already exists
        existing_original_url = db.query(URL_INFO).filter(URL_INFO.original_url == original_url).first()
        if existing_original_url:
            return {
            "status_code": 200, 
            "message": "URL has been shortened before successfully",
            "original_url": original_url,
            "shortened_url": existing_original_url.shortened_url,
            "url_hash": existing_original_url.url_hash
        }

        # Check if custom_back_half exists already
        if custom_back_half and db.query(URL_INFO).filter(URL_INFO.url_hash == custom_back_half).first():
            return {
                "status_code": 404, 
                "message": "The specified custom back half already exists for another url",
            } 

        # Check if custom back half was supplied and it is not available in the database
        if custom_back_half and not (db.query(URL_INFO).filter(URL_INFO.url_hash == custom_back_half).first()):
            url_hash = custom_back_half

        # Check if custom back half is not supplied and origianl url is not in database
        if not custom_back_half and not db.query(URL_INFO).filter(URL_INFO.original_url == original_url).first():
            original_link_byte_form = bytes(original_url, LINK_SHORTENER_ENCODING_SCHEME)
            url_hash = hashlib.sha256(original_link_byte_form).hexdigest()[:10]
    
        #Check if link with hash already exists then rehash the original url
        existing_hash = db.query(URL_INFO).filter(URL_INFO.url_hash == url_hash).first()
        if existing_hash:
            re_hash_byte_form = bytes(existing_hash.url_hash, LINK_SHORTENER_ENCODING_SCHEME)
            url_hash = hashlib.sha256(re_hash_byte_form).hexdigest()[:10]
        
        shortened_url = f"{API_BASE_URL}/{url_hash}"

        new_url = URL_INFO(
            original_url=original_url,
            shortened_url= shortened_url,
            url_hash = url_hash
        )

        db.add(new_url)
        db.commit()
        db.refresh(new_url)
        db.close()

        return{
            "status_code": 200, 
            "message": "URL shortened successfully",
            "original_url": original_url,
            "shortened_url": shortened_url,
            "url_hash": url_hash
        }

    except Exception as e:

        return{
            "status_code": 404, 
            "message": "URL shortening failed"
        }


@router.get("/{shortened_url}")
async def redirect_shortened_url(shortened_url: str, db : Session = Depends(get_db_session)):
    """
    Redirects the user to the original URL associated with the provided shortened URL.

    Args:
        db: The database session dependency obtained from `get_db_session`.

    Returns:
        None

    Raises:
        HTTPException: If the shortened URL is not found in the database.
    """

    redirect_url = db.query(URL_INFO).filter(URL_INFO.url_hash == shortened_url).first()
    original_url = redirect_url.original_url
    if original_url:

        return RedirectResponse(url=original_url, status_code=307)
    
    else:
        return{
            "status_code": 404, 
            "message": "Requested URL not found"
        }

