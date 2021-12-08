import sqlite3
from sqlite3.dbapi2 import Connection, connect
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="O campo username não pode ser em branco"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        nullable=True,
        help="O campo password não pode ser em branco"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_name(data['username']):
            return {"message": "Usuario já existe"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "Usuario criado com sucesso"}, 201

