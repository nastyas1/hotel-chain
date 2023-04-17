import flask
from flask import request, jsonify

from . import db_session
from data.hotels import Hotel

blueprint = flask.Blueprint('hotels_api', __name__, template_folder='templates')


@blueprint.route('/api/hotels')
def get_hotels():
    db_sess = db_session.create_session()
    hotels = db_sess.query(Hotel).all()
    return jsonify(
        {'hotels': [item.to_dict(only=('id', 'name', 'coordinate')) for item in hotels]})


@blueprint.route('/api/hotels/<int:hotel_id>', methods=['GET'])
def get_one_news(hotel_id):
    db_sess = db_session.create_session()
    hotel = db_sess.query(Hotel).get(hotel_id)
    if not hotel:
        return jsonify({'error': 'Not found'})
    return jsonify({'hotel': hotel.to_dict(only=('id', 'name', 'coordinate'))})


@blueprint.route('/api/hotels', methods=['POST'])
def create_hotel():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'coordinate']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()

    hotel = Hotel(
        id=request.json['id'],
        name=request.json['name'],
        coordinate=request.json['coordinate']
    )
    db_sess.add(hotel)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    db_sess = db_session.create_session()
    hotel = db_sess.query(Hotel).get(hotel_id)
    if not hotel:
        return jsonify({'error': 'Not found'})
    db_sess.delete(hotel)
    db_sess.commit()
    return jsonify({'success': 'OK'})
