from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

data = 'Name: Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края, Sum: <=3_000_000 RUB, Type: grant, Link: {link}'

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

def answer(req):
    llm = auth_llm(auth_t)

    ans_messages = [
        SystemMessage(
            content="Ты - бот для помощи предпринимателям. Вот несколько примеров твоей работы: "
                    "request1: 'Name: Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края, Sum: <=3_000_000 RUB, Type: grant, Link: {link}'"
                    "answer1: 'Для Вас лучше всего подойдёт грантовый способ поддержки - Вы можете получить грант по программе: \"Государственная прогрмма поддержки малого и среднего бизнеса Краснодарского края\" на сумму до 3 млн. рублей по сслыке {link}'"
                    "request2: 'Name: Услуги НКО \"Экология РФ\", Type: workforce, Link: {link}'"
                    "answer2: 'Вы можете воспользоваться услугами НКО \"Экология РФ\", пожалуйста, обратитесь по ссылке {link}'"
        )
    ]

    ans_messages.append(HumanMessage(content=req))
    res = llm.invoke(ans_messages)