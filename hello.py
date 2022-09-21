# pipenv install flask 
# pipenv shell 
# python3 nombre archivo.py

from flask import Flask, render_template #Importando Flask para permitirnos crear una aplicacion


app = Flask(__name__) #Creando una nueva instancia de la clase Flask llamada "app"

@app.route('/') #El decorador '@' asocia esa ruta con la funcion que vamos a tener inmediatamente
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/hola/<nombre>') #para mi ruta hola/___ se va a pasar como variable nombre
def hola(nombre):
    return f'Hola {nombre}, cómo estás?'

@app.route('/hello/<name>/<int:j>')
def hello(name, j):
    # en lugar de devolver una cadena devolvemos el resultado de un render template
    return render_template('hola.html', nombre=name, cantidad =j)


if __name__ == "__main__": #asegura que el archivo se esta ejecutando directamente y no desde un modulo diferente
    app.run(debug=True) #ejecuta la aplicacion 

