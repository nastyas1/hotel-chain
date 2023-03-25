import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from db_session import SqlAlchemyBase


class HotelNumber(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'hotel_number'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    number = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    free_time = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True) 

    hotel_id = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("hotel.id"))
    hotel = orm.relationship('Hotel')
    
    
    def __repr__(self):
        return f'<Hotel> {self.id} {self.number} {self.free_time}'

