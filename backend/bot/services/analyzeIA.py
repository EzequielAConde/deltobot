from transformers import pipeline

analizadorSentimiento = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyzeFeeling(texto: str) -> str:
    try:
        resultado = analizadorSentimiento(texto[:512])[0]
        etiqueta = resultado['label']
        confianza = resultado['score']

        estrellas = int(etiqueta.split()[0])
        if estrellas <= 2:
            sentimiento = "negativo"
        elif estrellas == 3:
            sentimiento = "neutral"
        else:
            sentimiento = "positivo"

        explicacion = {
            "positivo": "✨ Parece que estás de buen ánimo. ¡Eso es genial!",
            "neutral": "😐 Tu conversación muestra un tono equilibrado.",
            "negativo": "😞 Parece que hubo algunos momentos difíciles en la conversación.",
        }[sentimiento]

        return (
            f"🧠 Sentimiento detectado: *{sentimiento.capitalize()}* ({confianza:.2%} de confianza)\n"
            f"{explicacion}"
        )
    except Exception as e:
        return f"❌ No pude analizar el sentimiento. Error: {e}"
