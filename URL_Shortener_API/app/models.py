from sqlalchemy import Column, Integer, String
from .db import Base

# this is the table that store the url data along with shortened url
class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True)
