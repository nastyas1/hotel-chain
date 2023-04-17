import flask
from flask import request, jsonify

from .. import db_session
from data.hotel_numbers import HotelNumber

blueprint = flask.Blueprint('hotel_numbers_api', __name__, template_folder='templates')


@blueprint.route('/api/hotel_numbers')
def get_hotel_numbers():
    db_sess = db_session.create_session()
    hotel_numbers = db_sess.query(HotelNumber).all()
    return jsonify(
        {'hotel_numbers': [item.to_dict(only=('id', 'number', 'free_time')) for item in hotel_numbers]})


@blueprint.route('/api/hotel_numbers/<int:hotel_numbers_id>', methods=['GET'])
def get_one_hotel_number(hotel_numbers_id):
    db_sess = db_session.create_session()
    hotel_numbers = db_sess.query(HotelNumber).get(hotel_numbers_id)
    if not hotel_numbers:
        return jsonify({'error': 'Not found'})
    return jsonify({'hotel_numbers': hotel_numbers.to_dict(only=('id', 'number', 'free_time', 'hotel.id'))})


@blueprint.route('/api/hotel_numbers', methods=['POST'])
def create_hotel_number():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'number', 'free_time', 'hotel.id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()

    hotel_number = HotelNumber(
        id=request.json['id'],
        number=request.json['number'],
        feee_timr=request.json['free_time'],
        hotel_id=request.json['hotel.id']
    )
    db_sess.add(hotel_number)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/hotel_numbers/<int:hotel_number_id>', methods=['DELETE'])
def delete_hotel_number(hotel_number_id):
    db_sess = db_session.create_session()
    hotel_number = db_sess.query(HotelNumber).get(hotel_number_id)
    if not hotel_number:
        return jsonify({'error': 'Not found'})
    db_sess.delete(hotel_number)
    db_sess.commit()
    return jsonify({'success': 'OK'})
