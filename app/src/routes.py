import re
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from .models import Entity
from . import db

main = Blueprint('main', __name__)

@main.route('/entity', methods=['POST'])
def create_entity():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    errors = []

    if not name or len(name.split()) < 2:
        errors.append("Nome deve conter nome e sobrenome.")

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email or not re.match(email_regex, email):
        errors.append("Email inválido.")
    else:
        existing_entity = Entity.query.filter_by(email=email).first()
        if existing_entity:
            errors.append("Email já está em uso.")

    password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not password or not re.match(password_regex, password):
        errors.append("Senha deve ter no mínimo 8 caracteres, com pelo menos uma letra maiúscula, um número e um caractere especial.")

    if errors:
        return jsonify({'errors': errors}), 400
    
    hashed_password = generate_password_hash(password)
    new_entity = Entity(name=name, email=email, password=hashed_password)
    db.session.add(new_entity)
    db.session.commit()

    # Retornar os dados recebidos como JSON
    return jsonify({'id': new_entity.id}), 201
