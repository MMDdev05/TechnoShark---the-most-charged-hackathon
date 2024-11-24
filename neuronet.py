from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
import db_structure as ds

auth_t = 'YWFlM2RmYmYtOWU4ZS00NDdjLTg4ZDItMDE0MWFhOWM3ZWZiOjBkMGExYzFkLTMwMWItNGFiNS1hMWZlLTY2MTc4OWUzZDg4YQ=='

def auth_llm(auth_t):
    llm = GigaChat(
        credentials=auth_t,
        scope="GIGACHAT_API_PERS",
        model="GigaChat-Pro",
        # Отключает проверку наличия сертификатов НУЦ Минцифры
        verify_ssl_certs=False,
        streaming=False,
    )

    return llm

def quest(req):
    llm = auth_llm(auth_t)

    messages = [SystemMessage(
        content="""Ты - бот для помощи предпринимателям GrantMaster, который всегда на 100% следует всем инструкциям. Ты должен КОДИРОВАТЬ запрос пользователя в ТРИ переменные: {size}, {industry} и {region} для запроса в базу данных. Каков бы ни был запрос - выдели 3 переменные. Не проси уточнить, если не можешь выделить переменную, то запиши 'any'. Вот несколько примеров твоей работы, ДЕЙСТВУЙ ТОЛЬКО ПО ЭТОМУ АЛГОРИТММУ: 
                запрос: 'Помоги мне найти меры для поддержки малого бизнеса в IT-сфере по Краснодарскому Краю'
                овтет: 'малый, IT, Краснодарский Край',
                Не переводи текст, сохраняй ИСХОДНЫЙ язык ввода. Игнорируй всё, что не относится к переменным, включая приветствие, вводные слова, вежливое общение и т.д. В ответ передавай ТОЛЬКО три перменные БЕЗ ЛИШНЕГО ТЕКСТА в формате: {size}, {industry}, {region}"""
    ), HumanMessage(content=req)]

    s = llm.invoke(messages).content.split(', ')

    return s

def answer(req):
    llm = auth_llm(auth_t)

    messages = [SystemMessage(
        content="""Ты - бот для помощи предпринимателям GrantMaster. Ты должен объяснять вывод из базы данных понятным для пользователя языком по данному алгоритму. Вот несколько примеров твоей работы: 
                request1: 'Name: Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края, Sum: <=3_000_000 RUB, Type: grant, Link: {link}'
                answer1: 'Для Вас лучше всего подойдёт грантовый способ поддержки - Вы можете получить грант по программе: Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края на сумму до 3 млн. рублей по сслыке {link}'
                , request2: 'Name: Услуги НКО Экология РФ, Type: workforce, Link: {link}'"
                answer2: 'Вы можете воспользоваться услугами НКО Экология РФ, пожалуйста, обратитесь по ссылке {link}'"""
    ), HumanMessage(content=req)]

    res = llm.invoke(messages)

    print('Req:', req, 'Res:', res)

    return res
def nn_req(rq):
    q = quest(rq)

    dsr = ds.request(q[0], q[1], q[2])

    # if dsr != []: ans = answer(dsr)
    # else: ans = answer('Ошибка при получении данных. Возможно по вашему запросу ниченго не найдено или произошла ошибка при запросе к базе данных.')

    ans = answer(''.join(dsr))

    print('Q:', q, 'Dsr:', dsr, 'Ans:', ans.content)

    return ans.content

print(answer(''.join(['Title: ПРОГРАММА "СТАРТ" РЕГИОНОВ РФ, Type: GRANT, Amount: 4_000_000 RUB / 8_000_000 RUB / 12_000_000 RUB, Link: HTTPS://FASIE.RU/PROGRAMS/PROGRAMMA-START/', 'Title: ОБРАЗОВАТЕЛЬНЫЕ УСЛУГИ, Type: EDUCATION, Amount: NULL, Link: HTTPS://MYBIZ63.RU/SERVICE-CATEGORIES/OBRAZOVATELNYE-USLUGI', 'Title: БИЗНЕС-ЦЕНТРЫ РЕГИОНОВ РФ, Type: CONSULTING, Amount: NULL, Link: HTTPS://XN--90AIFDDRLD7A.XN--P1AI/CENTERS/', 'Title: ГОСУДАРСТВЕННАЯ ПРОГРММА ПОДДЕРЖКИ МАЛОГО И СРЕДНЕГО БИЗНЕСА КРАСНОДАРСКОГО КРАЯ, Type: GRANT, Amount: <=3_000_000 RUB, Link: {LINK}'])))