import datetime
 
from sqlalchemy import (
    Sequence,
    DateTime,
    Column,
    Integer,
    Text
    )
from .meta import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('msid', optional=True), primary_key=True)
    text = Column(Text, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
 
    def __init__(self, text):
        self.text = text