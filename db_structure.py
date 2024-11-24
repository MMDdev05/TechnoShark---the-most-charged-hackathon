from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer, ForeignKey, or_, and_
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

engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def request(size, industry, region):
    size = size.upper()
    industry = industry.upper()
    region = region.upper()
    r = []

    data = session.query(Common).filter(and_(or_(str(Common.size).upper() == size, size == 'ANY', str(Common.size).upper() == 'ANY'),
                 or_(str(Common.industry).upper() == industry, industry == 'ANY', str(Common.industry).upper() == 'ANY'),
                 or_(str(Common.region).upper() == region, region == 'ANY', str(Common.region).upper() == 'ANY')
                 )).all()

    for log in data:

        help_log = session.query(Help).filter(log.help_id == Help.id).first()

        r.append(f'Title: {help_log.title}, Type: {help_log.type}, Amount: {help_log.amount}, Link: {help_log.link}')

    return r

# print(request('малый', 'IT', 'Краснодарский Край'))