import flask
from flask import request, jsonify

from . import db_session
from .users import User

blueprint = flask.Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {'users': [item.to_dict(only=('id', 'name', 'email')) for item in users]})


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(news_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(news_id)
    if not users:
        return jsonify({'error': 'Not found'})
    return jsonify({'users': users.to_dict(only=('id', 'name', 'email', 'about'))})


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'email', 'about', 'hashed_password', 'hotel_number.id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()

    users = User(
        id=request.json['id'],
        name=request.json['name'],
        email=request.json['email'],
        about=request.json['about'],
        hashed_password=request.json['hashed_password'],
        hotel_number_id=request.json['hotel_number.id']
    )
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_user(users_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(users_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})
