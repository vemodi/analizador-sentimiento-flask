from flask import Flask, render_template, request, jsonify 
from analizador import clasificar_sentimiento # Importamos la función de VADER

app = Flask(__name__)

# RUTA PRINCIPAL (Para la interfaz HTML con Bootstrap)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Establecer valores por defecto (Neutral) para la carga inicial (GET)
    resultado_analisis = {
        'sentimiento': 'Neutral 😐 (Inicial)',
        'polaridad': 0.0,
        'clase_css': 'resultado-neutral',
        'color_hex': '#f4c20d' # Amarillo/Ocre
    }
    
    # ----------------------------------------------------
    # LÓGICA DE PROCESAMIENTO (POST) - INTERFAZ WEB
    # ----------------------------------------------------
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        
        if texto:
            # VADER hace la clasificación aquí
            sentimiento, polaridad = clasificar_sentimiento(texto)
            
            # Lógica de asignación de CSS/Color para la interfaz
            clase_css = "resultado-neutral"
            color_hex = "#f4c20d"

            if "Positivo" in sentimiento:
                clase_css = "resultado-positivo"
                color_hex = "#4CAF50" # Verde
            elif "Negativo" in sentimiento:
                clase_css = "resultado-negativo"
                color_hex = "#ff6b6b" # Rojo

            # Empaquetamos el resultado final
            resultado_analisis = {
                'sentimiento': sentimiento,
                'polaridad': polaridad,
                'clase_css': clase_css,
                'color_hex': color_hex
            }
        
    # ATENCIÓN: El template index.html espera la variable 'resultado'.
    # Corregido: antes tenías 'resultado_final', lo cual causaría un error.
    return render_template('index.html', resultado=resultado_analisis)

# 2. NUEVA RUTA: Endpoint para la API REST (Devuelve JSON)
@app.route('/api/analizar', methods=['POST'])
def api_analizar():
    # Aseguramos que la petición es JSON
    if not request.is_json:
        return jsonify({"error": "La petición debe ser de tipo application/json"}), 400

    # Obtenemos el cuerpo JSON de la petición
    data = request.get_json()
    texto = data.get('texto')

    if not texto:
        return jsonify({"error": "Campo 'texto' es requerido en el JSON."}), 400

    # Usamos la misma función de análisis VADER
    sentimiento, polaridad = clasificar_sentimiento(texto)

    # Devolvemos el resultado en formato JSON
    respuesta = {
        "texto_analizado": texto,
        "sentimiento_final": sentimiento.split(' ')[0], # Solo la palabra (Positivo/Negativo/Neutral)
        "polaridad_compound": round(polaridad, 4),
        "modelo": "VADER ES"
    }
    
    # 200 OK
    return jsonify(respuesta), 200

if __name__ == '__main__':
    # Ejecución local (el puerto $PORT es usado por Gunicorn en Render)
    app.run(debug=True)