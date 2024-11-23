from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

data = 'Help Type: type, Link: link, Examples: ex, Region: reg, Size: size, Industry: ind'

# Авторизация в GigaChat
llm = GigaChat(
    credentials="YWFlM2RmYmYtOWU4ZS00NDdjLTg4ZDItMDE0MWFhOWM3ZWZiOjlmNmE2OTE2LWY4MzEtNGU2NS1iMGM3LWE4MDI0MGQ0ZjdmYQ==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    # Отключает проверку наличия сертификатов НУЦ Минцифры
    verify_ssl_certs=False,
    streaming=False,
)

messages = [
    SystemMessage(
        content="Ты - бот для помощи предпринимателям. Вот несколько примеров твоей работы: "
                "request: 'Help Type: grant, Link: {link}, Region: {reg}'"
                "answer: 'Для вас лучше всего подойдёт грантовый способ поддержки'"
    )
]

while(True):
    user_input = input("Пользователь: ")
    if user_input == "пока":
      break
    messages.append(HumanMessage(content=user_input))
    res = llm.invoke(messages)
    messages.append(res)
    print("GigaChat: ", res.content)