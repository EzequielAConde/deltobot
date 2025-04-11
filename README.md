# 🤖 DELTOBOT  
_Asistente virtual retro para Telegram + Dashboard web en tiempo real_

---

## 📌 ¿Qué es DELTOBOT?

DELTOBOT es un bot interactivo para **Telegram**, potenciado con **Inteligencia Artificial**, que ofrece clima, análisis emocional, conversación libre y más. Todo conectado a un **dashboard estilo retro** con datos en tiempo real usando **Firebase**.

---

## 🧠 Funciones principales

### En Telegram

- `/start`: Inicia el bot.
- **Clima**: Consultá el clima de cualquier ciudad, con pronóstico y plan divertido sugerido por IA.
- **Contador**: Guarda la cantidad de interacciones por usuario.
- **Conversación libre**: Chateá con una IA y pedí análisis emocional de la charla.
- **Firebase**: Guarda nombre, contador e historial de países consultados.

### En la Web

- **Dashboard retro** en React:
  - Lista de usuarios e interacciones.
  - Países más consultados.
  - Pronóstico semanal.
  - Plan generado por IA.

---

## 🛠️ Tecnologías utilizadas

- **Python** – Lógica del bot.
- **FastAPI** – API para datos meteorológicos y análisis.
- **React** – Frontend estilo retro (pixel icons, fondo animado).
- **Firebase** – Base de datos en tiempo real.
- **OpenWeatherMap API** – Fuente de datos climáticos.
- **Cohere API** – Generación de texto + análisis emocional.

---

## 🗂️ Estructura del proyecto
```
deltobot/
├── backend/
│   ├── bot/           
│   ├── api/           
├── frontend/
│
│README.md
│requirements.txt
│start.py
```

## 🔧 Configuración Firebase

1. Crear proyecto en [Firebase Console](https://console.firebase.google.com).
2. Activar **Cloud Firestore** o **Realtime Database** (modo prueba para desarrollo).
3. Ir a `Configuración > Cuentas de servicio > Admin SDK`.
4. Generar clave privada y guardarla en backend/bot/firebase_key.json (mas adelante)


Instalación

1. Abrir cmd e ir hasta el Desktop
2. ejecutar: mkdir DeltBot
3. ejecutar: cd DeltoBot
4. ejecutar: git clone https://github.com/EzequielAConde/deltobot.git
5. ejecutar: cd deltobot (esto para estar dentro de la desarrollo sin subcarpetas)
6. ejecutar: code . (para abrir el visual Studio)
7. En la raiz ejecutar: py -m venv .venv
8. moverse al frontend: cd frontend
9. ejecutar: npm install
10. Volver a la raiz: cd..
11. en la raiz ejecutar: .venv\Scripts\activate
12. estando en el entorno virtual
13. ejecutar: pip install -r requirements.txt
14. Agregar Clave al firebase_key.json
15. cuando termine de instalar ejecutar: python start.py
