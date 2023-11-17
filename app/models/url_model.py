"""

URL INFORMATION TABLES

"""
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import(
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    UniqueConstraint,
)
from sqlalchemy.sql import func

from app.database import Base

class URL_INFO(Base):
    """
    The URL information table

    """

    __tablename__ = "url"
    id: int = Column(Integer, primary_key=True, index=True)
    original_url: String = Column(String(255), nullable=False, unique=True, index=True)
    shortened_url: String  = Column(String(255), nullable=False, unique=True)
    url_hash: String = Column(String(255), nullable=False, unique=True)
    created_date: DateTime = Column(DateTime, server_default=func.now())
    modified_date: DateTime = Column(DateTime, onupdate=func.now())
    is_deleted: bool = Column(Boolean, default=False)