from flask import Flask, render_template, request
from analizador import clasificar_sentimiento 

app = Flask(__name__)

# RUTA PRINCIPAL
@app.route('/', methods=['GET', 'POST'])
def index():
    # Establecer valores por defecto (Neutral) para la carga inicial (GET)
    resultado_analisis = {
        'sentimiento': 'Neutral 😊',
        'polaridad': 0.0,
        'clase_css': 'resultado-neutral',
        'color_hex': '#f4c20d' # Amarillo/Ocre, el color del Neutral
    }
    
    # ----------------------------------------------------
    # LÓGICA DE PROCESAMIENTO (POST)
    # ----------------------------------------------------
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        
        if texto:
            sentimiento, polaridad = clasificar_sentimiento(texto)
            
            # Asignar clase CSS y color basada en el resultado del modelo ML
            clase_css = "resultado-neutral"
            color_hex = "#f4c20d" # Amarillo

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

# Recuerda eliminar o comentar la línea app.run(debug=True) para el despliegue
# if __name__ == '__main__':
#     app.run(debug=True)