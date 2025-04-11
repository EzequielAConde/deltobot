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

Instalación

1. Abrir cmd y ejecutar(con el nombre que corresponda): cd %USERPROFILE%\Desktop
2. ejecutar: mkdir DeltBot
3. ejecutar: cd DeltoBot
4. ejecutar: git clone https://github.com/EzequielAConde/deltobot.git
5. ejecutar: code . (para abrir el visual Studio)
6. En la raiz ejecutar: python -m venv .venv
7. moverse al frontend: cd frontend
8. ejecutar: npm install
9. Volver a la raiz: cd..
10. en la raiz ejecutar: venv\Scripts\activate
11. estando en el entorno virtual
12. ejecutar: pip install -r requirements.txt
13. cuando termine de instalar ejecutar: python start.py



