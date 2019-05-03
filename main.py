#!usr/bin/python

from flask import (Flask, render_template, redirect, url_for, request, jsonify)
import serial
import requests
app = Flask(__name__)
s = serial.Serial("COM7")     #"/dev/ttyACM0")





@app.route("/")
def hello():

    h, t = get_serial_data()
    light = get_light_data()
    print(h)
    print(t)
    resp = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp-273.15)*(9/5)+32)

    hum = weather['humidity']

    return render_template("index.html", h=h, t=t, temp1=temp1, hum=hum, light=light)

def get_serial_data():
        s.write('A'.encode("ascii"))
        msg = s.readline().decode("ascii")
        msg = msg.split(',')
        h = msg[0]
        t = msg[1]
        return h, t




@app.route("/turn_on", methods=["POST"])
def button1():
    s.write('C'.encode("ascii"))
    h, t = get_serial_data()
    resp = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/turn_off", methods=["POST"])
def button2():
    s.write('D'.encode("ascii"))
    h, t = get_serial_data()
    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/sensor_on", methods=["POST"])
def button3():
    s.write('E'.encode("ascii"))
    s.write('A'.encode("ascii"))
    msg2 = s.readline().decode("ascii")
    msg2 = msg2.split(',')
    h = msg2[0]
    t = msg2[1]

    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/sensor_off", methods=["POST"])
def button4():
    s.write('F'.encode("ascii"))
    s.write('A'.encode("ascii"))
    msg2 = s.readline().decode("ascii")
    msg2 = msg2.split(',')
    h = msg2[0]
    t = msg2[1]

    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)


@app.route("/data.json", methods=["GET"])
def json_data():

    h, t = get_serial_data()

    data = {"temp": t, "humidity": h}

    return jsonify(data)

@app.route("/light.data", methods=["GET"])
def light_data():

    light = get_light_data()

    data1 = {"light": light}

    return jsonify(data1)

def get_light_data():
    s.write('G'.encode("ascii"))
    msg = s.readline().decode("ascii")

    return msg


@app.route("/message", methods=["POST"])
def message():
    message = request.form['message']

    cmd = "B%s\n" % message
    s.write(cmd.encode("ascii"))

    return render_template("index.html")

@app.route("/error", methods=["POST"])
def error():
    error = request.form['error']
    print(error)
    cmd = "H%s\n" % error
    s.write(cmd.encode("ascii"))

    return render_template("index.html")

#def get_remote_data():

 #   info = request.get("http://localhost:5001/data.json")
 #   values = info.json()
 #   temp = values['temp']
 #   hum = values['humidity']

 #   return temp, hum

app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)