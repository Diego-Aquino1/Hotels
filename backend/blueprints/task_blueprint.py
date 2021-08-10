from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('hotel_blueprint', __name__)

model = TaskModel()


@task_blueprint.route('/hotel/add_rate', methods=['POST'])
@cross_origin()
def create_taskru():
    content = model.add_rate(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Mensaje'], request.json['Calificacion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_rate', methods=['POST'])
@cross_origin()
def delete_taskru():
    return jsonify(model.delete_rate(int(request.json['Idrateus'])))

@task_blueprint.route('/hotel/get_rate', methods=['POST'])
@cross_origin()
def taskru():
    return jsonify(model.get_rate(int(request.json['Idrateus'])))

@task_blueprint.route('/hotel/get_rates', methods=['POST'])
@cross_origin()
def tasksru():
    return jsonify(model.get_rates())


#######################################


@task_blueprint.route('/hotel/add_form', methods=['POST'])
@cross_origin()
def create_taskcu():
    content = model.add_form(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Mensaje'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_form', methods=['POST'])
@cross_origin()
def delete_taskcu():
    return jsonify(model.delete_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_form', methods=['POST'])
@cross_origin()
def taskcu():
    return jsonify(model.get_form(int(request.json['Idcontactus'])))

@task_blueprint.route('/hotel/get_forms', methods=['POST'])
@cross_origin()
def taskscu():
    return jsonify(model.get_forms())


#######################################


@task_blueprint.route('/hotel/add_guest_h1', methods=['POST'])
@cross_origin()
def create_taskh1():
    content = model.add_guest1(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h1', methods=['POST'])
@cross_origin()
def delete_taskh1():
    return jsonify(model.delete_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h1', methods=['POST'])
@cross_origin()
def taskh1():
    return jsonify(model.get_guest1(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h1', methods=['POST'])
@cross_origin()
def tasksh1():
    return jsonify(model.get_guests1())


#######################################


@task_blueprint.route('/hotel/hotel2/reserva', methods=['GET','POST'])
@cross_origin()
def create_taskh2():
    if request.method == 'POST':
        content = model.add_guest2(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return render_template("Reserva2.html")

@task_blueprint.route('/hotel/delete_guest_h2', methods=['POST'])
@cross_origin()
def delete_taskh2():
    return jsonify(model.delete_guest2(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h2', methods=['POST'])
@cross_origin()
def taskh2():
    return jsonify(model.get_guest2(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h2', methods=['POST'])
@cross_origin()
def tasksh2():
    return jsonify(model.get_guests2())


#######################################


@task_blueprint.route('/hotel/add_guest_h3', methods=['POST'])
@cross_origin()
def create_taskh3():
    content = model.add_guest3(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h3', methods=['POST'])
@cross_origin()
def delete_taskh3():
    return jsonify(model.delete_guest3(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h3', methods=['POST'])
@cross_origin()
def taskh3():
    return jsonify(model.get_guest3(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h3', methods=['POST'])
@cross_origin()
def tasksh3():
    return jsonify(model.get_guests3())


#######################################


@task_blueprint.route('/hotel/add_guest_h4', methods=['POST'])
@cross_origin()
def create_taskh4():
    content = model.add_guest4(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h4', methods=['POST'])
@cross_origin()
def delete_taskh4():
    return jsonify(model.delete_guest4(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h4', methods=['POST'])
@cross_origin()
def taskh4():
    return jsonify(model.get_guest4(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h4', methods=['POST'])
@cross_origin()
def tasksh4():
    return jsonify(model.get_guests4())


#######################################


@task_blueprint.route('/hotel/add_guest_h5', methods=['POST'])
@cross_origin()
def create_taskh5():
    content = model.add_guest5(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h5', methods=['POST'])
@cross_origin()
def delete_taskh5():
    return jsonify(model.delete_guest5(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h5', methods=['POST'])
@cross_origin()
def taskh5():
    return jsonify(model.get_guest5(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h5', methods=['POST'])
@cross_origin()
def tasksh5():
    return jsonify(model.get_guests5())


#######################################


@task_blueprint.route('/hotel/add_guest_h6', methods=['POST'])
@cross_origin()
def create_taskh6():
    content = model.add_guest6(request.json['Apellidos'], request.json['Nombres'], request.json['Email'], request.json['Celular'], request.json['Habitaciones'], request.json['Descripcion'])
    return jsonify(content)

@task_blueprint.route('/hotel/delete_guest_h6', methods=['POST'])
@cross_origin()
def delete_taskh6():
    return jsonify(model.delete_guest6(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guest_h6', methods=['POST'])
@cross_origin()
def taskh6():
    return jsonify(model.get_guest6(int(request.json['ID'])))

@task_blueprint.route('/hotel/get_guests_h6', methods=['POST'])
@cross_origin()
def tasksh6():
    return jsonify(model.get_guests6())

