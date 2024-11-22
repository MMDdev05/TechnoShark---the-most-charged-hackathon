from transformers import pipeline

data = 'help: Grant, help_link: index.html, region: Adigea, size: medium, industry: Computer production'

messages = [
    {"role": "system", "content": f"Ты должен объяснить пользователю следующие данные:\n{data}"},
    {"role": "user", "content": "Какой способ помощи мне подходит и по какой сслыке его можно получить?"},
]
chatbot = pipeline("text-generation", model="mistralai/Mistral-Nemo-Instruct-2407", max_new_tokens=128)
chatbot(messages)