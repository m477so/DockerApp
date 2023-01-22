from flask import Flask, render_template, request
import requests
from pycountry import countries

app = Flask(__name__, template_folder='/home/msojka/weatherapp')

@app.route("/")
def weather():
    return render_template("weather.html")

@app.route("/result", methods=["POST"])
def result():
    city = request.form["city"]
    api_key = "69634c93182fd22ac67dc085e98bb09b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    weather_data = requests.get(url).json()
    country_code = weather_data.get('sys', {}).get('country')
    if country_code:
        country_name = countries.get(alpha_2=country_code).name
    else:
        country_name = None
    return render_template("result.html", weather_data=weather_data, country_name=country_name)

if __name__ == "__main__":
    app.run(debug=True)