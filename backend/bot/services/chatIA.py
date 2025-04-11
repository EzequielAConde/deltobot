import cohere
import config

clienteCohere = cohere.Client(config.COHERE_API_KEY)

def talkWithIa(mensaje: str) -> str:
    prompt = (
        f"Respondé de forma simpática, divertida, no mas de 100 caracteres y en español si o si al siguiente mensaje:\n "
        f"{mensaje}"
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
        return "🤖 Uy, no pude responder ahora. Intentá de nuevo más tarde."
