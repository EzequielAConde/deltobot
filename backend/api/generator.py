import cohere

COHERE_KEY = "kxP1jU1fbmAppdwU5H5MipDh1QBp1JK8oO4DZR2g"

co = cohere.Client(COHERE_KEY)

def generatePlans (pais: str) -> str:
    prompt = (
        f"Estoy planeando un viaje a {pais}. ¿Qué planes divertidos o actividades recomendás hacer allí, "
        f"teniendo en cuenta su clima típico? no pasarse de los 200 caracteres Respondé en tono gracioso y SI o SI en español, tiene que ser respuestas cortas"
    )

    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"No se pudo generar una respuesta de IA: {str(e)}"
