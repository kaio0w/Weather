from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'fd6d476fc15892392e27ce45b805660e'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cidade = request.form['cidade']
        r = requests.get(url.format(cidade, api_key)).json()
        clima = {
            'cidade': cidade,
            'temperatura': round(r['main']['temp'] - 273.15, 2),  # Convertendo para Celsius
            'descricao': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        return render_template('index.html', clima=clima)
    return render_template('index.html', clima=None)

if __name__ == '__main__':
    app.run(debug=True)
