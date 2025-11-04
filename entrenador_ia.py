import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib # Herramienta para guardar el modelo

# --- 1. DATOS DE ENTRENAMIENTO (Tu primer dataset) ---
# 0 = Negativo, 1 = Positivo
data = {
    'texto': [
        "Me encanta este proyecto, funciona de maravilla.",
        "Esto es horrible, no lo recomiendo a nadie.",
        "La aplicacion tiene errores, no me deja avanzar.",
        "La interfaz es muy buena y facil de usar.",
        "Este tutorial fue confuso y perdi mi tiempo.",
        "El código está bien organizado, lo felicito.",
        "No me gusto el servicio, fue muy lento.",
        "El producto llegó a tiempo y en excelente estado."
    ],
    'sentimiento': [1, 0, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# --- 2. PRE-PROCESAMIENTO: Convertir Texto a Números ---
# La IA solo entiende números. El CountVectorizer convierte palabras en vectores numéricos.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['texto']) # X son los datos (el texto)
y = df['sentimiento'] # y son las etiquetas (0 o 1)

# --- 3. ENTRENAMIENTO DEL MODELO ---
# Usamos el clasificador Naive Bayes, simple y muy rápido para texto.
modelo = MultinomialNB()
modelo.fit(X, y)

# --- 4. GUARDAR EL MODELO ENTRENADO ---
# Guardamos el modelo (el "cerebro" que aprendió) y el vectorizador (el "traductor")
# Los guardamos como archivos .pkl para poder usarlos en app.py
joblib.dump(modelo, 'modelo_ia.pkl')
joblib.dump(vectorizer, 'vectorizer_ia.pkl')

print("¡Entrenamiento completado!")
print("Archivos 'modelo_ia.pkl' y 'vectorizer_ia.pkl' creados.")