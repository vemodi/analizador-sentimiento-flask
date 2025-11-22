import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib # Herramienta para guardar el modelo

# --- 1. DATOS DE ENTRENAMIENTO (Dataset Ampliado) ---
# 0 = Negativo, 1 = Positivo
data = {
    'texto': [
        "Me encanta este proyecto, funciona de maravilla.", # Positivo
        "Esto es horrible, no lo recomiendo a nadie.", # Negativo
        "La aplicacion tiene errores, no me deja avanzar.", # Negativo
        "La interfaz es muy buena y facil de usar.", # Positivo
        "Este tutorial fue confuso y perdi mi tiempo.", # Negativo
        "El código está bien organizado, lo felicito.", # Positivo
        "No me gusto el servicio, fue muy lento.", # Negativo
        "El producto llegó a tiempo y en excelente estado.", # Positivo
        
        # --- NUEVOS EJEMPLOS NEUTRALES (CORRECCIÓN) ---
        "El servidor Flask corre en el puerto 5000.", # Neutral (0)
        "Necesitamos instalar la librería scikit-learn y pandas.", # Neutral (0)
        "Revisa el archivo .gitignore antes de subir los cambios.", # Neutral (0)
        "La carpeta templates debe contener el archivo index.html.", # Neutral (0)
        
        # --- NUEVOS EJEMPLOS EXTREMOS (PARA ROBUSTEZ) ---
        "Es la mejor experiencia que he tenido, felicitaciones.", # Positivo
        "Es un completo desastre, nunca debí haber comprado esto.", # Negativo
    ],
    'sentimiento': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]
}
# ... el resto del código del entrenador_ia.py sigue igual ...

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