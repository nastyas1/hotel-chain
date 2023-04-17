from data.db_session import create_session
from flask_restful import abort, Resource
from flask import jsonify
from parse_args_users import parser
from data.users import User


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'email', 'about',))})

    def post(self, user_id):
        args = parser.parse_args()
        abort_if_users_not_found(user_id)
        session = create_session()
        user = {
            'name': args['name'],
            'email': args['email'],
            'about': args['about']
        }
        session.query(User).filter(User.id == user_id).update(user)
        session.commit()
        return jsonify({'success': 'OK'})


    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'email', 'about')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        user = User(
            name=args['name'],
            email=args['email'],
            about=args['about']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_users_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
