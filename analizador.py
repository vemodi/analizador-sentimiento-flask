# =================================================================
# ANALIZADOR DE SENTIMIENTO AVANZADO (VADER Localizado y Final)
# =================================================================
import os
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- PASO CRUCIAL: USAR LA RUTA LOCAL DEL DICCIONARIO ESPAÑOL ---
# El archivo 'vader_lexicon_es.txt' DEBE estar en la misma carpeta que analizador.py
try:
    # Ruta del archivo de léxico español (ruta relativa segura)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    spanish_lexicon_path = os.path.join(current_dir, 'vader_lexicon_es.txt')

    # Inicializar VADER con el diccionario español
    analyzer = SentimentIntensityAnalyzer(lexicon_file=spanish_lexicon_path)
except Exception:
    # Usar el analizador por defecto como fallback (inglés)
    analyzer = SentimentIntensityAnalyzer()

def clasificar_sentimiento(texto):
    """
    Clasifica el sentimiento de un texto dado utilizando el modelo VADER en español.
    """
    
    # Preprocesamiento simple para VADER
    texto = re.sub(r'[^\w\s\.\,\!\?]', '', texto.lower())
    
    # Obtener el puntaje de polaridad de VADER
    vs = analyzer.polarity_scores(texto)
    polaridad = vs['compound']

    # Lógica de Clasificación VADER:
    if polaridad >= 0.05:
        sentimiento = "Positivo 😊 (FINAL)"
    elif polaridad <= -0.05:
        sentimiento = "Negativo 😠 (FINAL)"
    else:
        sentimiento = "Neutral 😐 (FINAL)"

    return sentimiento, polaridad