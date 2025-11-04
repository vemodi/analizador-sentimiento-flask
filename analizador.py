# Importamos la herramienta VADER y la utilidad para manejar colecciones de datos
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# import json # Ya no es necesario

# --- 1. Diccionario de Sentimientos en Español (Parte de la Solución) ---
spanish_sentiment_lexicon = {
    'excelente': 3.5,
    'encanto': 2.9,
    'perfecto': 3.0,
    'bueno': 1.5,
    'feliz': 2.5,
    'odio': -3.4,
    'frustracion': -3.0,
    'terrible': -3.5,
    'malo': -1.8,
    'problema': -2.0,
    'avanzar': 0.5, 
    'perdi': -1.5 
}

# --- 2. Adaptación de VADER (SOLUCIÓN AL ERROR) ---

# Inicializamos el analizador SIN pasarle el diccionario al inicio
analizador_vader = SentimentIntensityAnalyzer()

# AÑADIMOS nuestro diccionario español al diccionario interno de VADER
analizador_vader.lexicon.update(spanish_sentiment_lexicon) 

# --- 3. Función de Clasificación (Igual que antes) ---
def clasificar_sentimiento(texto):
    """
    Función que recibe un texto en español y devuelve su sentimiento.
    """
    
    texto_procesado = texto.lower() 
    
    # 1. Obtiene la puntuación de sentimiento de VADER
    vs = analizador_vader.polarity_scores(texto_procesado)
    
    # 2. La polaridad será el valor 'compound' (combinado)
    polaridad = vs['compound']
    
    # 3. Clasificamos el resultado 
    if polaridad > 0.1:
        resultado = "Positivo 😊"
    elif polaridad < -0.1:
        resultado = "Negativo 😠"
    else:
        resultado = "Neutral 😐"
        
    return resultado, polaridad