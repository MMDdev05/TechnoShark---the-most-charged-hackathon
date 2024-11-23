from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_structure import Base, Common, Help

engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    req = input("Action (write/read/close) > ")

    if req == 'write':
        req2 = '0'

        w_help_type = input('help type > ')
        w_help_link = input('help link > ')
        w_help_examples = input('help examples > ')
        w_region = input('region > ')
        w_size = input('size > ')
        w_industry = input('industry > ')

        new_help = Help(type=w_help_type, link=w_help_link, examples=w_help_examples)
        session.add(new_help)
        session.commit()

        new_common = Common(size=w_size, help_id=new_help.id, industry=w_industry, region=w_region)
        session.add(new_common)
        session.commit()


    elif req == 'read':

        data = session.query(Common).all()

        for log in data:
            help_entry = session.query(Help).filter(Help.id == log.help_id).first()

            print(f'\nHelp Type: {help_entry.type}, Link: {help_entry.link}, Examples: {help_entry.examples}, '

                  f'Region: {log.region}, Size: {log.size}, Industry: {log.industry}\n')

    else: break