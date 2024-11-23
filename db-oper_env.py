from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
from db_structure import Base, Common, Help

def request(size, industry, region):
    r = []

    data = session.query(Common).filter(and_(or_(Common.size == size, size == 'any'), or_(Common.industry == industry, industry == 'any'), or_(Common.region == region, region == 'any'))).all()

    for log in data:
        help_data = session.query(Help).filter(Help.id == log.help_id).all()

        for help_log in help_data:
            r.append(f'Title: {help_log.title}, Type: {help_log.type}, Amount: {help_log.amount}, Link: {help_log.link}')

    return r

engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    req = input("Action (write/del/read/close) > ")

    if req == 'write':
        w_help_title = input('help title > ')
        w_help_type = input('help type > ')
        w_help_amount = input('help amount > ')
        w_help_link = input('help link > ')
        w_region = input('region > ')
        w_size = input('size > ')
        w_industry = input('industry > ')

        new_help = Help(type=w_help_type, link=w_help_link, title=w_help_title, amount=w_help_amount)
        session.add(new_help)
        session.commit()

        new_common = Common(size=w_size, help_id=new_help.id, industry=w_industry, region=w_region)
        session.add(new_common)
        session.commit()

    elif req == 'del':
        index = int(input('> '))
        product = session.query(Common).filter(Common.id == index).delete()
        session.commit()  # Применяем изменения
        print(f'Object with id "{index}" has been deleted')

    elif req == 'read':

        data = session.query(Common).all()

        for log in data:
            help_log = session.query(Help).filter(Help.id == log.help_id).first()

            if log != None:
                print(f'Title: {help_log.title}, Type: {help_log.type}, Amount: {help_log.amount}, Link: {help_log.link}')

    else: break