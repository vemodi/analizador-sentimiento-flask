from flask import Flask, render_template, request
from analizador import clasificar_sentimiento 

app = Flask(__name__)

# RUTA PRINCIPAL
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_analisis = None
    
    if request.method == 'POST':
        texto = request.form.get('texto_input')
        
        if texto:
            sentimiento, polaridad = clasificar_sentimiento(texto)
            
            # --- NUEVA LÓGICA: Asignar clase CSS y color ---
            clase_css = "resultado-neutral"
            color_hex = "#f4c20d" # Amarillo

            if "Positivo" in sentimiento:
                clase_css = "resultado-positivo"
                color_hex = "#4CAF50" # Verde
            elif "Negativo" in sentimiento:
                clase_css = "resultado-negativo"
                color_hex = "#ff6b6b" # Rojo

            # 4. Empaquetamos el resultado para enviarlo al HTML
            resultado_analisis = {
                'sentimiento': sentimiento,
                'polaridad': polaridad,
                'clase_css': clase_css,    # <-- NUEVO
                'color_hex': color_hex     # <-- NUEVO
            }
        
        # El resto del código de manejo de errores sigue igual...

    return render_template('index.html', resultado_final=resultado_analisis)

#if __name__ == '__main__':
 #   app.run(debug=True)

 if __name__ == '__main__':
    # app.run(debug=True) <--- ELIMINA o COMENTA esta línea para el despliegue
    pass # Puedes dejarlo así si quieres