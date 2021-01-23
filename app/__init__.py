from flask import Flask
# from flask_pymongo import PyMongo
from pyrebase import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = '6s5d7f8g'

admin_user = 'Admin123'
admin_pass = '123Admin'

# app.config.from_object(Config)

firebaseConfig = {
    'apiKey': "AIzaSyBDYHhwQpYvpNLszMM4UzKyKULnamKWZyk",
    'authDomain': "sololearn-76c84.firebaseapp.com",
    'databaseURL': "https://sololearn-76c84-default-rtdb.firebaseio.com",
    'projectId': "sololearn-76c84",
    'storageBucket': "sololearn-76c84.appspot.com",
    'messagingSenderId': "598254086506",
    'appId': "1:598254086506:web:27afbedb202a4f76001d13",
    'measurementId' : "G-8PELQ9RN6V"
}

firebase = pyrebase.initialize_app(firebaseConfig);

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

from app import routes