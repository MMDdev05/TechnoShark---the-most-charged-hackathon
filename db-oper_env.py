from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
from db_structure import Base, Common, Help

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

        new_help = Help(type=w_help_type.upper(), link=w_help_link.upper(), title=w_help_title.upper(), amount=w_help_amount.upper())
        session.add(new_help)
        session.commit()

        new_common = Common(size=w_size.upper(), help_id=new_help.id, industry=w_industry.upper(), region=w_region.upper())
        session.add(new_common)
        session.commit()

    elif req == 'del':
        index = int(input('> '))
        data = session.query(Common).all()

        for log in data:
            session.query(Common).filter(log.id == index).delete()
            session.query(Help).filter(Help.id == index).delete()

        session.commit()  # Применяем изменения
        print(f'Object with id "{index}" has been deleted')

    elif req == 'read':

        data = session.query(Common).all()

        for log in data:
            help_log = session.query(Help).filter(log.help_id == Help.id).first()

            print(f'Title: {help_log.title}, Type: {help_log.type}, Amount: {help_log.amount}, Link: {help_log.link}')
            print(f'Id: {log.id}, Size: {log.size}, Industry: {log.industry}, Region: {log.region}')

    else: break