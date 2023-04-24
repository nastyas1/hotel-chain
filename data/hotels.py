import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from data.db_sess import SqlAlchemyBase
from sqlalchemy import orm



class Hotel(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'hotel'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    coordinate = sqlalchemy.Column(sqlalchemy.String, nullable=True)



    def __repr__(self):
        return f'<Hotel> {self.coordinate}'
