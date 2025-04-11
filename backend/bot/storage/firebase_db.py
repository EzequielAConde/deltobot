import firebase_admin
from firebase_admin import credentials, firestore


if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
usuarios_ref = db.collection('usuarios')

def saveUser(user_id, nombre, pais=None, contador=0):
    doc_ref = usuarios_ref.document(str(user_id))
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        paises = set(data.get("paises_buscados", []))
        if pais:
            paises.add(pais)
        doc_ref.update({
            "nombre": nombre,
            "paises_buscados": list(paises)
        })
    else:
        doc_ref.set({
            "nombre": nombre,
            "paises_buscados": [pais] if pais else [],
            "contador": contador
        })

def updateCounter(user_id, valor):
    usuarios_ref.document(str(user_id)).update({"contador": valor})

def getUser(user_id):
    doc = usuarios_ref.document(str(user_id)).get()
    return doc.to_dict() if doc.exists else None

def increaseCounter(user_id, nombre):
    doc_ref = usuarios_ref.document(str(user_id))
    doc = doc_ref.get()

    if doc.exists:
        data = doc.to_dict()
        nuevo_valor = data.get("contador", 0) + 1
        doc_ref.update({"contador": nuevo_valor})
    else:
        nuevo_valor = 1
        doc_ref.set({
            "nombre": nombre,
            "contador": nuevo_valor,
            "paises_buscados": []
        })

    return nuevo_valor
