# =================================================================
# ANALIZADOR DE SENTIMIENTO AVANZADO (VADER Español Corregido)
# =================================================================
import os
import re

# Importamos el Analizador de VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- PASO CRUCIAL: CARGAR EL LÉXICO EN ESPAÑOL ---
# VADER está optimizado para inglés por defecto. Debemos indicarle dónde está
# el diccionario de español y cargarlo manualmente.

# Usamos la ubicación predeterminada del léxico de VADER.
# Buscamos el directorio donde está instalado el paquete vaderSentiment
vader_lexicon_dir = os.path.dirname(os.path.abspath(__file__))

# Subimos dos niveles hasta el directorio de site-packages de VADER
for _ in range(3):
    vader_lexicon_dir = os.path.dirname(vader_lexicon_dir)
vader_lexicon_dir = os.path.join(vader_lexicon_dir, 'vaderSentiment')

# Ruta al archivo de léxico español
spanish_lexicon_file = os.path.join(vader_lexicon_dir, 'vader_lexicon_es.txt')

# Inicializar VADER con el diccionario español
analyzer = SentimentIntensityAnalyzer(lexicon_file=spanish_lexicon_file)

# ----------------------------------------------------
# Nota: La función de clasificación sigue siendo la misma:
# ----------------------------------------------------

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
        sentimiento = "Positivo 😊 (ES)"
    elif polaridad <= -0.05:
        sentimiento = "Negativo 😠 (ES)"
    else:
        sentimiento = "Neutral 😐 (ES)"

    return sentimiento, polaridad