from sqlalchemy import Column, Integer, String, Text
from backend.database import Base  

class CodeReview(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text)
    review = Column(Text)
    score = Column(String)
    language = Column(String)