from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

auth_t = 'YWFlM2RmYmYtOWU4ZS00NDdjLTg4ZDItMDE0MWFhOWM3ZWZiOjlmNmE2OTE2LWY4MzEtNGU2NS1iMGM3LWE4MDI0MGQ0ZjdmYQ=='

def auth_llm(auth_t):
    llm = GigaChat(
        credentials=auth_t,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        # Отключает проверку наличия сертификатов НУЦ Минцифры
        verify_ssl_certs=False,
        streaming=False,
    )

    return llm

def quest(req):
    llm = auth_llm(auth_t)

    messages = [SystemMessage(
        content="Ты - бот для помощи предпринимателям GrantMaster. Ты должен КОДИРОВАТЬ запрос пользователя в ТРИ переменные: size, industry и region для запроса в базу данных. Вот несколько примеров твоей работы, ДЕЙСТВУЙ ТОЛЬКО ПО ЭТОМУ АЛГОРИТММУ: "
                "request1: 'Помоги мне найти меры для поддержки малого бизнеса в IT-сфере по Краснодарскому Краю'"
                "answer1: 'малый, IT, Краснодарский Край'"
                "request2: 'Помоги мне найти меры для поддержки любого бизнеса в сфере розничной торговли по всей России'"
                "answer2: 'any, Торговля, any'"
                "request_common: 'Help me to find suitable {size} business support solution in domain of {industry} in {region} area'"
                "answer_common: '{size}, {industry}, {region}'"
    ), HumanMessage(content=req)]

    s = llm.invoke(messages).content.split(', ')

    return s[0], s[1], s[2]

def answer(req):
    llm = auth_llm(auth_t)

    messages = [SystemMessage(
        content="Ты - бот для помощи предпринимателям GrantMaster. Ты должен объяснять вывод из базы данных понятным для пользователя языком по данному алгоритму. Вот несколько примеров твоей работы: "
                "request1: 'Name: Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края, Sum: <=3_000_000 RUB, Type: grant, Link: {link}'"
                "answer1: 'Для Вас лучше всего подойдёт грантовый способ поддержки - Вы можете получить грант по программе: \"Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края\" на сумму до 3 млн. рублей по сслыке {link}'"
                "request2: 'Name: Услуги НКО \"Экология РФ\", Type: workforce, Link: {link}'"
                "answer2: 'Вы можете воспользоваться услугами НКО \"Экология РФ\", пожалуйста, обратитесь по ссылке {link}'"
    ), HumanMessage(content=req)]

    return llm.invoke(messages)