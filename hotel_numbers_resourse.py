from data.db_session import create_session
from flask_restful import abort, Resource
from flask import jsonify
from parse_args_hotels import parser
from data.hotel_numbers import HotelNumber


class HotelNumbersResource(Resource):
    def get(self, hotel_number_id):
        """
        возвращает один номер отеля по id
        """
        abort_if_hotels_not_found(hotel_number_id)
        session = create_session()
        hotel_number = session.query(HotelNumber).get(hotel_number_id)
        return jsonify({'hotel number': hotel_number.to_dict(
            only=('number', 'free_time'))})

    def post(self, hotel_number_id):
        """
        записывает в базу данных номер отеля по id
        """
        args = parser.parse_args()
        abort_if_hotels_not_found(hotel_number_id)
        session = create_session()
        hotel_number = {
            'number': args['number'],
            'free_time': args['free_time']
        }
        session.query(HotelNumber).filter(HotelNumber.id == hotel_number_id).update(hotel_number)
        session.commit()
        return jsonify({'success': 'OK'})


    def delete(self, hotel_number_id):
        """
        удаляет данные номер отеля по id
        """
        abort_if_hotels_not_found(hotel_number_id)
        session = create_session()
        hotel_number = session.query(HotelNumber).get(hotel_number_id)
        session.delete(hotel_number)
        session.commit()
        return jsonify({'success': 'OK'})


class HotelNumbersListResource(Resource):
    def get(self):
        session = create_session()
        hotel_numbers = session.query(HotelNumber).all()
        return jsonify({'hotel_numbers': [item.to_dict(
            only=('number', 'free_time')) for item in hotel_numbers]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        hotel_number = HotelNumber(
            number=args['number'],
            free_time=args['free_time']
        )
        session.add(hotel_number)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_hotels_not_found(hotel_number_id):
    """
    возвращает сообщение об ошибке, если id номера отеля не существует
    """
    session = create_session()
    hotel_number = session.query(HotelNumber).get(hotel_number_id)
    if not hotel_number:
        abort(404, message=f"Hotel number {hotel_number_id} not found")
