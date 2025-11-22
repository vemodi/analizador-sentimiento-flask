from flask import Flask, render_template, request
from analizador import clasificar_sentimiento # Importamos la función de VADER

app = Flask(__name__)

# RUTA PRINCIPAL
@app.route('/', methods=['GET', 'POST'])
def index():
    # Establecer valores por defecto (Neutral) para la carga inicial (GET)
    # Los valores iniciales deben coincidir con la lógica de VADER (polaridad 0 es neutral)
    resultado_analisis = {
        'sentimiento': 'Neutral 😐 (Inicial)',
        'polaridad': 0.0,
        'clase_css': 'resultado-neutral',
        'color_hex': '#f4c20d' # Amarillo/Ocre
    }
    
    # ----------------------------------------------------
    # LÓGICA DE PROCESAMIENTO (POST)
    # ----------------------------------------------------
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        
        if texto:
            # VADER hace la clasificación aquí
            sentimiento, polaridad = clasificar_sentimiento(texto)
            
            # ----------------------------------------------------
            # NUEVA LÓGICA DE ASIGNACIÓN DE COLOR (Más simple)
            # ----------------------------------------------------
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
        
    return render_template('index.html', resultado_final=resultado_analisis)

# if __name__ == '__main__':
#     app.run(debug=True)