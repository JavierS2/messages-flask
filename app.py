from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configuración de la base de datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ejemplo'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registros', methods=['POST'])
def registros():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        # Conexión a la base de datos
        conn = mysql.connect()
        cursor = conn.cursor()

        # Insertar los datos en la base de datos
        cursor.execute("INSERT INTO registros (nombre, correo, mensaje) VALUES (%s, %s, %s)", (nombre, correo, mensaje))
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

        # Redirigir a la página de visualización
        return redirect(url_for('visualizar'))

@app.route('/registros',methods=['GET'])
def visualizar():
    # Conexión a la base de datos
    conn = mysql.connect()
    cursor = conn.cursor()

    # Obtener todos los registros
    cursor.execute("SELECT nombre, correo, mensaje FROM registros")
    registros = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    # Pasar los registros a la plantilla
    return render_template('visualizar.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
