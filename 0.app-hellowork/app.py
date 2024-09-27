# Ejercicio 1: crea una aplicacion web basica con flask que, al ser ejecutada, inicia un servidor local en el puerto 5000. cuando visita la ruta principal (https://localhost:5000/),el servidor respondera con un mensaje HTML que dice "Hello, World Flask".

# se importa el modulo Flask desde el paquete flask
from flask import Flask

# crea una instancia de la clase Flask
# el argumento __name__ le dice a Flask
# que utilice el nombre del archivo actual main.py
app = Flask(__name__)

# este es un decorador que define una ruta
# corresponde a la pagina Principal del app
@app.route("/")
# cuando alguien visite app (por ejemplo, http://localhost:5000/),
# la funcion hello() sera ejecutada
def hello():
    return "<h1>Hello, World Flask !</h1>"

# solo se ejecute si el archivo es ejecutado directamente
# arranca la aplicacion Flask en modo de depuracion (debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=5000)