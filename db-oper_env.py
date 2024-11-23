from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_structure import Base, Common

engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    req = input("Action (write/read/close) > ")

    if req == 'write':
        req2 = '0'

        while req2 != 'commit':
            req2 = input('Action (commit/write) > ')

            if req2 == 'write':
                w_help = input('help > ')
                w_help_link = input('help_link > ')
                w_region = input('region > ')
                w_size = input('size > ')
                w_industry = input('industry > ')
                session.add(Common(help = w_help, help_link = w_help_link, region = w_region, size = w_size, industry = w_industry))

            elif req2 == 'commit':
                try:
                    session.commit()
                    print(f'# Data "{w_help, w_help_link, w_region, w_size, w_industry}" has been committed to Common')
                except: print('Error while committing, try to write data another time')

    elif req == 'read':
        data = session.query(Common).all()
        for log in data:
            print(f'help: {log.help}, help_link: {log.help_link}, region: {log.region}, size: {log.size}, industry: {log.industry}')

    else: break