from flask import Flask, render_template, request
from neuronet import nn_req  # Импортируйте вашу функцию из нейросети

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['message']  # Получите данные из формы
        response = nn_req(user_input)  # Вызовите функцию из нейросети

        return render_template('index.html', response=response)

    else: return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)