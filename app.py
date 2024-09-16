
from bottle import Bottle, template, static_file

app = Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/alumno')
def alumno():
    return template('alumno', nombre="Oliver Ronald", apellidoPaterno="Camacho", apellidoMaterno="Velasco", edad=45)

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
