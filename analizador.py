# =================================================================
# ANALIZADOR DE SENTIMIENTO AVANZADO (Basado en VADER)
# =================================================================

# Importamos el Analizador de VADER para el idioma español
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Creamos una instancia del analizador
# VADER es un modelo basado en reglas de léxico (palabras y su valor emocional)
analyzer = SentimentIntensityAnalyzer()

def clasificar_sentimiento(texto):
    """
    Clasifica el sentimiento de un texto dado utilizando el modelo VADER.
    Devuelve el sentimiento (Positivo/Negativo/Neutral) y la Polaridad.
    """
    
    # Obtener el puntaje de polaridad de VADER
    # 'compound' es la puntuación general normalizada entre -1 (negativo) y +1 (positivo)
    vs = analyzer.polarity_scores(texto)
    polaridad = vs['compound']

    # ----------------------------------------------------
    # Lógica de Clasificación de VADER:
    # ----------------------------------------------------
    
    # 1. POSITIVO: Puntaje > 0.05
    if polaridad >= 0.05:
        sentimiento = "Positivo 😊 (VADER)"
        
    # 2. NEGATIVO: Puntaje < -0.05
    elif polaridad <= -0.05:
        sentimiento = "Negativo 😠 (VADER)"
        
    # 3. NEUTRAL: Puntaje entre -0.05 y 0.05
    else:
        sentimiento = "Neutral 😐 (VADER)"

    # Devolvemos el sentimiento clasificado y la puntuación de polaridad
    return sentimiento, polaridad

# NOTA: Ya no necesitamos cargar el modelo ni el vectorizador aquí.