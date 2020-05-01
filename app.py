from flask import Flask, render_template, request
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = "randoidgasgasga"


@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=888e5560b176e058e6168a1919c61a3e"
        city = request.form['city']
        r = requests.get(url.format(city)).json()
        weather_data = {
            'city':city,
            "temperature":r['main']['temp'],
            "description":r['weather'][0]['description'],
            "icon":r['weather'][0]['icon']
        }
        return weather_data
    return render_template("index.html", weather=weather_data) 


if __name__ == "__main__":
    app.run(debug=True)