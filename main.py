from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class B_size(Base):
    __tablename__ = "size_table"
    size = Column(String, primary_key=True)
    help = relationship("Common_table", backref="help")

class Industry(Base):
    __tablename__ = "industry_table"
    industry = Column(String, primary_key=True)
    help = relationship("Common_table", backref="help")

class Region(Base):
    __tablename__ = "region_table"
    region = Column(String, primary_key=True)
    help = relationship("Common_table", backref="help")

class Common_table(Base):
    __tablename__ = "common"
    help = Column(String, primary_key=True)
    size = relationship("B_size", backref='size')
    industry = relationship("Industry", backref='industry')
    region = relationship("Region", backref='region')