import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from data.db_sess import SqlAlchemyBase


class BusyDay(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'busy_day'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    arrive_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    departure_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hotel_id = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey("hotel.id"), nullable=False)

    hotel = orm.relationship('Hotel')

    def __repr__(self):
        return f'<Hotel busy:> {self.arrive_day} - {self.departure_day}'


# бронировать отель можно только с 00 до 00
# тогда для отображения, выбранный отель должен из своей бд
# отдать занятые дни
