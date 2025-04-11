import firebase_admin
from firebase_admin import credentials, firestore
import os

Credencial = os.path.join(os.path.dirname(__file__), '../bot/firebase_key.json')

if not firebase_admin._apps:
    cred = credentials.Certificate(Credencial)
    firebase_admin.initialize_app(cred)

db = firestore.client()
