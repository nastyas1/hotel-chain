from data.db_session import create_session
from flask_restful import abort, Resource
from flask import jsonify
from parse_args_hotels import parser
from data.hotels import Hotel


class HotelsResource(Resource):
    def get(self, hotel_id):
        """
        возвращает один отель по id
        """
        abort_if_hotels_not_found(hotel_id)
        session = create_session()
        hotel = session.query(Hotel).get(hotel_id)
        return jsonify({'hotel': hotel.to_dict(
            only=('name', 'coordinate'))})

    def post(self, hotel_id):
        """
        записывает в базу данных отель по id
        """
        args = parser.parse_args()
        abort_if_hotels_not_found(hotel_id)
        session = create_session()
        hotel = {
            'name': args['name'],
            'coordinate': args['coordinate']
        }
        session.query(Hotel).filter(Hotel.id == hotel_id).update(hotel)
        session.commit()
        return jsonify({'success': 'OK'})


    def delete(self, hotel_id):
        """
        удаляет данные отеля по id
        """
        abort_if_hotels_not_found(hotel_id)
        session = create_session()
        hotel = session.query(Hotel).get(hotel_id)
        session.delete(hotel)
        session.commit()
        return jsonify({'success': 'OK'})


class HotelsListResource(Resource):
    def get(self):
        session = create_session()
        hotels = session.query(Hotel).all()
        return jsonify({'hotels': [item.to_dict(
            only=('name', 'coordinate')) for item in hotels]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        hotel = Hotel(
            name=args['name'],
            coordinate=args['coordinate']
        )
        session.add(hotel)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_hotels_not_found(hotel_id):
    """
    возвращает сообщение об ошибке, если id отеля не существует
    """
    session = create_session()
    hotel = session.query(Hotel).get(hotel_id)
    if not hotel:
        abort(404, message=f"Hotel {hotel_id} not found")
