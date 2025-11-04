import joblib
# No necesitamos VADER ni el diccionario español, ¡usamos nuestro modelo!

# --- 1. CARGAR EL MODELO ENTRENADO ---
try:
    # Cargamos el modelo (el cerebro) y el vectorizador (el traductor)
    modelo = joblib.load('modelo_ia.pkl')
    vectorizer = joblib.load('vectorizer_ia.pkl')
except FileNotFoundError:
    print("Error: Los archivos del modelo (modelo_ia.pkl, vectorizer_ia.pkl) no se encontraron.")
    # Si hay error, salimos, ya que la IA no puede funcionar.
    exit()

# --- 2. FUNCIÓN DE CLASIFICACIÓN CON ML ---
def clasificar_sentimiento(texto):
    """
    Clasifica el texto usando el modelo de Machine Learning entrenado.
    """
    
    # 1. El texto se debe traducir al formato numérico que el modelo entiende
    # Usamos el mismo vectorizador que usamos para entrenar.
    texto_vectorizado = vectorizer.transform([texto]) 
    
    # 2. El modelo predice la etiqueta (0 o 1)
    prediccion = modelo.predict(texto_vectorizado)[0]
    
    # 3. Traducimos la predicción a un resultado legible
    if prediccion == 1:
        resultado = "Positivo 😊 (ML)"
    else: # predicion == 0
        resultado = "Negativo 😠 (ML)"
        
    # NOTA: Los modelos ML no dan una "polaridad" simple, solo la clase (0 o 1). 
    # Por eso devolvemos la clase y una puntuación simple (1 o 0).
    return resultado, float(prediccion)