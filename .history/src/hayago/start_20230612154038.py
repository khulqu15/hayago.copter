import pyrebase
import sys
import signal

config = {
    "apiKey": "AIzaSyBi8dJvahsGnlEJxt2XW9CbCVCZ_F8QbIA",
    "authDomain": "eco-enzym.firebaseapp.com",
    "databaseURL": "https://eco-enzym-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "eco-enzym",
    "storageBucket": "eco-enzym.appspot.com",
    "messagingSenderId": "1090135367285",
    "appId": "1:1090135367285:web:024ab437397e3ea199623c",
    "measurementId": "G-57LTEMH91G"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("app").child("copters").child("0").child("actived").set(True)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C or the program was terminated!')
    db.child("app").child("copters").child("0").child("actived").set(False)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

while True:
    pass 
