# 1. Traemos las herramientas (Mesero y Cocinero)
# Importamos la función clasificar_sentimiento de nuestro archivo 'analizador.py'
from analizador import clasificar_sentimiento 
from flask import Flask, request, jsonify, render_template
# [YA NO NECESITAS IMPORTAR TextBlob aquí]
#linea modificada en el segundo objetivo hay que eliminarla from textblob import TextBlob

# 2. Creamos la aplicación (Iniciamos el turno del Mesero)
app = Flask(__name__)

# --- Rutas (Las Mesas del Restaurante) ---

# 3. RUTA 1: La Página Principal (Mesa '/')
# Cuando alguien abre la dirección web principal (http://127.0.0.1:5000/)
@app.route('/')
def index():
    # Le decimos al Mesero que busque y muestre el archivo HTML.
    return render_template('index.html')

# 4. RUTA 2: El Servicio de Análisis (Mesa '/analizar_sentimiento')
# Aquí se envían los datos para que el cocinero trabaje.
# methods=['POST'] significa que esta ruta solo acepta datos enviados, no solo una visita.
@app.route('/analizar_sentimiento', methods=['POST'])
def analizar():
    # ... dentro de la función analizar()...

    # 5. El Mesero (Flask) toma la orden (el texto del usuario)
    data = request.get_json()
    texto = data.get('texto', '')

    # 6. Verificamos que no esté vacío (Manejo de errores básico)
    if not texto:
        return jsonify({'error': 'Por favor, introduce algún texto'}), 400

    # 7. ¡NUEVO CÓDIGO! El Mesero llama al Cocinero especializado (analizador.py)
    resultado, polaridad = clasificar_sentimiento(texto) 
    # La función clasificar_sentimiento nos devuelve el resultado y la polaridad.

    # 8. El Mesero devuelve el resultado final al usuario.
    return jsonify({
        'sentimiento': resultado,
        'polaridad': polaridad
    })

# ... el resto del código sigue igual ...

    # 9. El Mesero devuelve el resultado final al usuario.
    return jsonify({
        'sentimiento': resultado,
        'polaridad': polaridad
    })

# 10. Encendemos el horno (Iniciamos el servidor)
if __name__ == '__main__':
    app.run(debug=True)