from flask import Flask, render_template
import requests
app: Flask = Flask(__name__)


@app.route("/")
def hello():
    html_data = render_template("main.html", name="test")
    print(html_data)

    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()
    print(values['main'])

    return html_data




app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)