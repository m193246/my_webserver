#!/usr/bin/python3

from flask import (Flask, render_template, redirect, url_for, request, jsonify)
import serial
import requests
app = Flask(__name__)
#s = serial.Serial("COM7")     #"/dev/ttyACM0")





@app.route("/")
def hello():
#    s.write('A'.encode("ascii"))
 #   msg = s.readline().decode("ascii")
    #print("I got: ", msg)
    msg = msg.split(',')
    h = msg[0]
    t = msg[1]

    resp = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp-273.15)*(9/5)+32)

    return render_template("index.html", h=h, t=t,  temp1=temp1)

@app.route("/turn_on")
def button1():
#    s.write('B'.encode("ascii"))
#    s.write('A'.encode("ascii"))
#    msg1 = s.readline().decode("ascii")
    msg1 = msg1.split(',')
    h = msg1[0]
    t = msg1[1]

    resp = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/turn_off")
def button2():
#    s.write('C'.encode("ascii"))
#    s.write('A'.encode("ascii"))
#    msg2 = s.readline().decode("ascii")
    msg2 = msg2.split(',')
    h = msg2[0]
    t = msg2[1]

    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/sensor_on")
def button3():
#    s.write('D'.encode("ascii"))
#    s.write('A'.encode("ascii"))
#    msg2 = s.readline().decode("ascii")
    msg2 = msg2.split(',')
    h = msg2[0]
    t = msg2[1]

    resp = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baltimore&APPID=59d6f344ba349fa2eff07bd7b6571d6a')
    values = resp.json()

    weather = values['main']
    temp = weather['temp']
    temp1 = int((temp - 273.15) * (9 / 5) + 32)

    return render_template("index.html", h=h, t=t, temp1=temp1)

@app.route("/sensor_off")
def button4():
#    s.write('E'.encode("ascii"))
#    s.write('A'.encode("ascii"))
#    msg2 = s.readline().decode("ascii")
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
    data = {"temp": 65, "humidity": 25}

    return jsonify(data)


@app.route("/message", methods=["POST"])
def message():
    message = request.form['message']
    cmd = "B%s\n" % message
#    s.write(cmd.encode("ascii"))

    return render_template("index.html")

app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)
