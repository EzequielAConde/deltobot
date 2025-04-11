import cohere
import config

clienteCohere = cohere.Client(config.COHERE_API_KEY)

async def generateTips(ciudad: str, condicion: str) -> str:
    prompt = (
        f"El clima en {ciudad} está {condicion}. "
        "Dame solo *Recomendación* bien corta maximo 100 caracteres, práctica o curiosa sobre eso, en español. "
        "No des introducciones, solo la frase directamente."
    )

    try:
        respuesta = clienteCohere.generate(
            model="command",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        return respuesta.generations[0].text.strip()
    except Exception:
        return ""
