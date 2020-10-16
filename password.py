import sqlite3
from hashlib import sha256

AdminPassword = "123645"

connect = input("What is your password?\n")

while connect != AdminPassword:
    connet = input("What is your password?\n")
    if connect == "q":
        break

conn = sqlite3.connect('pass_manager.db')
def createPassword(passKey, service, adminPass):
    return sha256(adminPass.encode('utf-8') + service.lower().encode('utf-8') + passKey.encode('utf-8')).hexdigest()[:15]

def get_hex_key(adminPass, service):
    return sha256(adminPass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

def getPassword(adminPass, service):
    secretKey = get_hex_key(adminPass, service)
    cursor = conn.execute("SELECT * from KEYS WHERE passKey=" + "" + secretKey + "")
    
