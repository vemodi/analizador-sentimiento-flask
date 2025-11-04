# analizador-sentimiento-flask
Analizador de sentimiento en español con Python Flask y Vader adaptado.

# 🚀 Analizador de Sentimiento en Español (Full Stack + IA)

Este proyecto es una aplicación web sencilla desarrollada con **Python y Flask** que permite a los usuarios ingresar texto en español para determinar su **sentimiento** (Positivo, Negativo o Neutral) utilizando técnicas de Procesamiento de Lenguaje Natural (PNL).

---

## 💡 Características y Tecnologías

El proyecto fue desarrollado como una guía desde cero para integrar el desarrollo web con la Inteligencia Artificial.

| Componente | Tecnología | Función |
| :--- | :--- | :--- |
| **Backend (Servidor)** | `Flask` | Servidor web (Manejo de rutas y lógica). |
| **Frontend (Interfaz)** | `HTML` y `CSS` | Interfaz de usuario y manejo de formularios. |
| **Inteligencia Artificial** | `VADER Sentiment` (Adaptado) | Modelo de PNL que clasifica el texto. |
| **Organización** | `Python Modularidad` | Lógica de IA separada (`analizador.py`) de la lógica del servidor (`app.py`). |

---

## 🛠️ Guía de Instalación (Para Ejecutar en Local)

Sigue estos pasos para instalar y correr la aplicación en tu máquina local.

### Prerrequisitos

* Python 3.x instalado.

### Pasos

1.  **Clonar el Repositorio**
    Abre tu terminal y descarga el código:
    ```bash
    git clone [https://github.com/vemodi/analizador-sentimiento-flask.git](https://github.com/vemodi/analizador-sentimiento-flask.git)
    cd analizador-sentimiento-flask
    ```

2.  **Crear el Entorno Virtual**
    Se recomienda usar un entorno virtual para aislar las dependencias:
    ```bash
    py -m venv venv
    source venv/Scripts/activate 
    ```

3.  **Instalar Dependencias**
    Instala las librerías `Flask` y `vaderSentiment`:
    ```bash
    py -m pip install flask vaderSentiment
    ```

4.  **Ejecutar el Servidor**
    Asegúrate de estar dentro del entorno `(venv)` y ejecuta:
    ```bash
    python app.py
    ```
    El servidor estará disponible en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## ⚙️ Funcionamiento del Modelo de IA

El corazón de este proyecto reside en el archivo `analizador.py`.

El análisis de sentimiento se realiza mediante la librería **VADER Sentiment**, la cual ha sido **adaptada manualmente** para el idioma español. El diccionario de palabras clave en español fue inyectado en el analizador para permitir una clasificación precisa de frases en español.

* **Reglas de Clasificación:**
    * **Positivo:** Polaridad Compuesta > 0.1
    * **Negativo:** Polaridad Compuesta < -0.1
    * **Neutral:** Polaridad Compuesta entre -0.1 y 0.1

---

## 👤 Autor

* [Veronica] - *Desarrollador Full Stack/IA*

---
