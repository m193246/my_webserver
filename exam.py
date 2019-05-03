import requests
import datetime
import hashlib
import serial
import random

s = serial.Serial("COM7")


def get_name():

    #print("Enter a Marvel hero: ")
    names = ["Thor", "Thanos", "Iron Man", "Deadpool", "Hulk", "Wolverine", "Ant-man"]
    super_hero_name = random.choice(names)

    public = "838d93462406b46abc48001411d6d1ae"

    private = "5c4d13013be321673ab98d0ea3930065683e38ce"

    ts = datetime.datetime.now().timestamp()

    input = str(ts)+private+public
    hash = hashlib.md5(input.encode('ascii')).hexdigest()

    query = "https://gateway.marvel.com:443/v1/public/characters?"
    query += "name=%s" % super_hero_name
    query += "&apikey=%s" % public
    query += "&hash=%s" % hash
    query += "&ts=%s" % ts

    print("public: %s, ts: %s, hash: %s" % (public, ts, hash))

    resp = requests.get(query)
    #print("Super Hero description: ")
    vals = resp.json()
    #data = vals["data"]
    #results = data["results"]
    #desc = results["description"]
    #print(desc)
    #try:
    print(vals["data"]["results"][0]["comics"]["available"])

    num = vals["data"]["results"][0]["comics"]["available"]

    return super_hero_name, num



    #except IndexError:
    #   print("Sorry %s is not a real hero" % super_hero_name)
    #import pdb
    #pdb.set_trace()

while 1:
    if s.read():
        name, num = get_name()
        print(name)
        print(num)

        s.write(str(name).encode("ascii"))

        s.write(str(num).encode("ascii"))
        s.write('\n'.encode("ascii"))

