from flask import Flask
from flask_mysqldb import MySQL, MySQLdb
from flask import request
from flask import render_template
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from flask import url_for, flash, redirect
from werkzeug.exceptions import abort

import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'hotelregister'

mysql = MySQL(app)

cors = CORS(app)

app.secret_key='secretkey'

#############################################

@app.route('/hotel')
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/hotel/5estrellas')
@cross_origin()
def hotels5():
    return render_template("Hoteles5.html")

@app.route('/hotel/hotelsnew')
@cross_origin()
def hotelsnew():
    return render_template("Hotelesnew.html")

@app.route('/hotel/contacts')
@cross_origin()
def contacts():
    return render_template("contacts.html")

############################################

@app.route('/hotel/hotel1')
@cross_origin()
def hotel1():
    return render_template("hotel1.html")

@app.route('/hotel/hotel1/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h1 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel1'))

    return render_template("Reserva1.html")

@app.route('/hotel/hotel1/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel1'))
    return render_template("Calificacion1.html")

@app.route('/hotel/hotel1/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus1():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel1'))
    return render_template("contactanos1.html")

#############################################

@app.route('/hotel/hotel2')
@cross_origin()
def hotel2():
    return render_template("hotel2.html")

@app.route('/hotel/hotel2/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva2():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h2 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel2'))

    return render_template("Reserva2.html")

@app.route('/hotel/hotel2/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion2():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel2'))

    return render_template("Calificacion2.html")


@app.route('/hotel/hotel2/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus2():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel2'))

    return render_template("contactanos2.html")

#############################################

@app.route('/hotel/hotel3')
@cross_origin()
def hotel3():
    return render_template("hotel3.html")

@app.route('/hotel/hotel3/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva3():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h3 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel3'))

    return render_template("Reserva3.html")

@app.route('/hotel/hotel3/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion3():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel3'))
    return render_template("Calificacion3.html")

@app.route('/hotel/hotel3/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus3():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel3'))
    return render_template("contactanos3.html")

#############################################

@app.route('/hotel/hotel4')
@cross_origin()
def hotel4():
    return render_template("hotel4.html")

@app.route('/hotel/hotel4/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva4():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h4 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel4'))
    return render_template("Reserva4.html")

@app.route('/hotel/hotel4/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion4():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel4'))
    return render_template("Calificacion4.html")

@app.route('/hotel/hotel4/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus4():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel4'))
    return render_template("contactanos4.html")

#############################################

@app.route('/hotel/hotel5')
@cross_origin()
def hotel5():
    return render_template("hotel5.html")

@app.route('/hotel/hotel5/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva5():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h5 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel5'))
    return render_template("Reserva5.html")

@app.route('/hotel/hotel5/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion5():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel5'))
    return render_template("Calificacion5.html")

@app.route('/hotel/hotel5/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus5():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel5'))
    return render_template("contactanos5.html")

#############################################

@app.route('/hotel/hotel6')
@cross_origin()
def hotel6():
    return render_template("hotel6.html")

@app.route('/hotel/hotel6/reserva', methods=('GET', 'POST'))
@cross_origin()
def reserva6():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Celular = request.form['Celular']
        Habitaciones = request.form['Habitaciones']
        Descripcion = request.form['Descripcion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO guests_h6 (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion) values (%s,%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Celular, Habitaciones, Descripcion))
        mysql.connection.commit()
        flash("Add Guest")
        return  redirect(url_for('hotel6'))
    return render_template("Reserva6.html")

@app.route('/hotel/hotel6/calificacion', methods=('GET', 'POST'))
@cross_origin()
def calificacion6():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        Calificacion = request.form['Calificacion']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO rateus (Apellidos, Nombres, Email, Mensaje, Calificacion) values (%s,%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje, Calificacion))
        mysql.connection.commit()
        flash("Add Rate")
        return  redirect(url_for('hotel6'))
    return render_template("Calificacion6.html")

@app.route('/hotel/hotel6/contactus', methods=('GET', 'POST'))
@cross_origin()
def contactus6():
    if request.method == 'POST':
        Apellidos = request.form['Apellidos']
        Nombres = request.form['Nombres']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contactus (Apellidos, Nombres, Email, Mensaje) values (%s,%s,%s,%s)', (Apellidos, Nombres, Email, Mensaje))
        mysql.connection.commit()
        flash("Add Form")
        return  redirect(url_for('hotel6'))
    return render_template("contactanos6.html")

#############################################

if __name__ == "__main__":
    app.run(debug=True)
