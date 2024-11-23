from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

class Base(DeclarativeBase):
    pass

class Help(Base):
    __tablename__ = "help_table"

    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String)
    amount = Column(String)
    link = Column(String)
    title = Column(String)

    commons = relationship("Common", back_populates="help", lazy='select')

class Common(Base):
    __tablename__ = "common_table"

    id = Column(Integer, primary_key=True, unique=True)
    help_id = Column(Integer, ForeignKey('help_table.id'))
    size = Column(String)
    industry = Column(String)
    region = Column(String)

    help = relationship("Help", back_populates="commons", lazy='select')