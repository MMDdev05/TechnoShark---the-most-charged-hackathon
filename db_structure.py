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

engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)


def request(size, industry, region):
    r = []

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(Common).filter(
        and_(or_(Common.size == size, size == 'any'), or_(Common.industry == industry, industry == 'any'),
             or_(Common.region == region, region == 'any'))).all()

    for log in data:
        help_data = session.query(Help).filter(Help.id == log.help_id).all()

        for help_log in help_data:
            r.append(
                f'Title: {help_log.title}, Type: {help_log.type}, Amount: {help_log.amount}, Link: {help_log.link}')

    return r