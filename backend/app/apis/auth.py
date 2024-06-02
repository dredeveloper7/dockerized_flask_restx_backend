# auth.py
from flask import request
from flask_restx import Namespace, Resource, fields
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models.user import User
from ..extensions import db

auth_ns = Namespace('auth', description='Authentication operations')

signup_model = auth_ns.model('Signup', {
    'email': fields.String(required=True, description='The email address'),
    'password': fields.String(required=True, description='The user password'),
})

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        if User.query.filter_by(email=email).first():
            return {'message': 'User already exists'}, 400

        bcrypt = Bcrypt()
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='The user email adress'),
    'password': fields.String(required=True, description='The user password'),
})

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        bcrypt = Bcrypt()
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401

@auth_ns.route('/protected')
class Protected(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        return {'message': f'Logged in as user {current_user_id}'}, 200
