import os
import re
import jwt
import datetime

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Entity
from . import db

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret_key')
TOKEN_EXPIRATION = {
    'short': datetime.timedelta(hours=24),
    'long': datetime.timedelta(days=30)
}

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

    return jsonify({'id': new_entity.id}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    stay_connected = data.get('stay_connected', False)

    if not email or not password:
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400
    
    user = Entity.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Email ou senha incorretos.'}), 401
    
    expiration = TOKEN_EXPIRATION['long'] if stay_connected else TOKEN_EXPIRATION['short']

    token_payload = {
        'email': user.email,
        'exp': datetime.datetime.utcnow() + expiration
    }

    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')

    return jsonify({'id': user.id, 'token': token}), 200

@main.route('/verify-token', methods=['GET'])
def verify_token():
    token = request.headers.get('Authorization')
    user_id = request.headers.get('x-forge-entity')

    if not token or not user_id:
        return jsonify({'error': 'Token e ID do usuário são obrigatórios.'}), 400
    
    if token.startswith('Bearer '):
        token = token[7:]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        token_email = payload.get('email')

        user = Entity.query.filter_by(id=user_id).first()
        if not user or user.email != token_email:
            return jsonify({'error': 'Token inválido ou não autorizado.'}), 401
        
        return jsonify({'message': 'Token é válido.'}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expirado.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Token inválido.'}), 401