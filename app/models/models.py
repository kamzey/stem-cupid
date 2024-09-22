from sqlalchemy import Column, Integer, String
from .database import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    url = Column(String)

class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

