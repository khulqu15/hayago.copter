import pyrebase

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