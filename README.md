# 🤖 DELTOBOT
**Tu asistente virtual retro en Telegram con IA, clima, emociones y datos en tiempo real.**

---

## 📌 Descripción

**DELTOBOT** es un bot de Telegram potenciado con Inteligencia Artificial que ofrece una experiencia interactiva, útil y entretenida. Con una estética retro y funcionalidades modernas, este asistente puede:

- Consultar el clima de cualquier ciudad con pronósticos y recomendaciones personalizadas.
- Llevar un contador individual de interacciones por usuario.
- Analizar el estado emocional de una conversación completa.
- Conversar libremente con una IA sobre cualquier tema.
- Mostrar un tablero web estilo retro con información actualizada en tiempo real.

Incluye un **frontend en React** que se conecta a **Firebase** para mostrar:
- El país más consultado.
- El pronóstico semanal.
- Un plan divertido generado por IA.

---

## 💪 Tecnologías utilizadas

- **Python**: Lógica principal del bot.
- **FastAPI**: API para exponer datos y procesar la información climática.
- **React**: Interfaz web con estilo retro (íconos pixelados y fondo animado).
- **Firebase**: Base de datos en tiempo real.
- **OpenWeatherMap API**: Fuente de datos meteorológicos.
- **Cohere API**: Análisis emocional y generación de texto por IA.

---

## 🗂️ Estructura del proyecto

```
deltobot/
├── backend/
│   ├── bot/           
│   ├── api/            
├── frontend/           
│
├── README.md
├── requirements.txt
├── start.py           
```

---

## ⚙️ Funcionalidades

### En Telegram

- **/start**: Inicia el bot.
- **Clima**: Consultá el clima de cualquier ciudad. Devuelve temperatura, pronóstico y un plan sugerido.
- **Contador**: Cada vez que lo presionás, suma uno y lo guarda por usuario.
- **Conversación libre**: Hablá con una IA y pedile que analice el estado emocional del diálogo.
- **Base de datos**: Se guarda nombre, contador e historial de países consultados en Firebase.

### En la Web

- **Dashboard retro** con:
  - Lista de usuarios e interacciones.
  - Países más buscados.
  - Pronóstico semanal del país más consultado.
  - Plan divertido sugerido por la IA.

---

## 🔧 Configuración de Firebase

1. Crear un proyecto en [Firebase Console](https://console.firebase.google.com).
2. Ir a **Cloud Firestore** o **Realtime Database** y crear la base de datos (modo prueba recomendado para desarrollo).
3. Navegar a:  
   `https://console.firebase.google.com/project/NOMBRE_DE_TU_PROYECTO/settings/serviceaccounts/adminsdk`
4. Generar una nueva clave privada.
5. Guardar el archivo JSON como `firebase_key.json` en la ruta:  
   `deltobot/backend/bot/firebase_key.json`

---

## 🖥️ Instalación y ejecución

1. Abrí la terminal (cmd) y dirigite al escritorio:
   ```bash
   mkdir Deltobot
   cd Deltobot
   git clone https://github.com/EzequielAConde/deltobot.git
   cd deltobot
   code .  # Abre Visual Studio Code
   ```

2. Crear y activar entorno virtual:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Instalar frontend:
   ```bash
   cd frontend
   npm install
   cd ..
   ```

5. Agregar el archivo `firebase_key.json` a la ruta `backend/bot/`.

6. Iniciar el bot:
   ```bash
   python start.py
   ```

---

Listo 🚀¡Ya tenés tu bot listo para funcionar!

