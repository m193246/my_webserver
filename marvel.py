import requests
import datetime
import hashlib

#print("Testing API")
print("Enter a Marvel hero: ")
super_hero_name = input()

public = "838d93462406b46abc48001411d6d1ae"

private = "5c4d13013be321673ab98d0ea3930065683e38ce"

ts = datetime.datetime.now().timestamp()

input = str(ts)+private+public
hash = hashlib.md5(input.encode('ascii')).hexdigest()

query = "https://gateway.marvel.com:443/v1/public/creators?"
query += "firstName=%s" % super_hero_name
query += "&apikey=%s" % public
query += "&hash=%s" % hash
query += "&ts=%s" % ts

print("public: %s, ts: %s, hash: %s" % (public, ts, hash))

resp = requests.get(query)
print("Super Hero description: ")
vals = resp.json()

try:
    print(vals["data"]["results"][0])#["description"])
except IndexError:
    print("Sorry %s is not a real hero" % super_hero_name)


#import pdb
#pdb.set_trace()