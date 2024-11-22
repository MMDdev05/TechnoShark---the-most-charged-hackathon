from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class Common(Base):
    __tablename__ = "common_table"
    help = Column(String, primary_key=True)
    help_link = Column(String)
    size = Column(String)
    industry = Column(String)
    region = Column(String)