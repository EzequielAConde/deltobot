🤖 DELTOBOT

Tu asistente virtual en Telegram con IA, clima, emociones y estilo retro.

Descripción

Deltobot es un bot de Telegram que utiliza Inteligencia Artificial para ayudarte a:

- Consultar el clima de cualquier ciudad con pronóstico y recomendaciones personalizadas.
- Llevar un contador de interacciones por usuario.
- Analizar el estado emocional de una conversación completa.
- Hablar con una IA sobre cualquier tema.
- Ver un tablero web retro con datos actualizados en tiempo real.

Además, incluye un frontend en **React** que muestra los datos almacenados en **Firebase**, como el país más buscado y el pronóstico semanal.

Tecnologías

- **Python**: Backend principal del bot.
- **FastAPI**: API para exponer los datos y procesar el clima.
- **React**: Interfaz visual estilo retro.
- **Firebase**: Base de datos en tiempo real.
- **OpenWeatherMap API**: Datos de clima.
- **Cohere API**: IA para generar texto y analizar emociones.

Estructura del proyecto

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

Funcionalidades

En Telegram:

- `/start`: Inicia el bot.
- Opción **Clima**: consultás cualquier ciudad y te devuelve clima, temperatura y un plan sugerido.
- Opción **Contador**: cada vez que lo apretás, suma uno y lo guarda por usuario.
- **Conversación libre**: hablás con una IA y podés pedirle el estado emocional del intercambio.
- **Base en Firebase**: almacena nombre, contador y países que consultaste.

En la web:

- Tablero con usuarios, contador y países más buscados.
- Pronóstico semanal del país más consultado.
- Plan divertido generado por IA para esa ciudad.
- Estética retro, con íconos pixelados y fondo animado.


Configuración de Firebase:

Crear un proyecto en Firebase
Ir a https://console.firebase.google.com.

Crear un nuevo proyecto.

🗄Crear la base de datos
Desde el panel del proyecto:

Ir a Cloud Firestore o Realtime Database.

Hacer clic en “Crear base de datos”.

Elegir el modo de seguridad (modo prueba recomendado para desarrollo).

Despues va a:
https://console.firebase.google.com/project/NOMBREDELABASE/settings/serviceaccounts/adminsdk

pone generar nueva clave privada, los datos de ese json se agregan mas adelante en deltobot\backend\bot que se encuentra el firebase_key.json

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



