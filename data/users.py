import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_sess import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(
        sqlalchemy.String, index=True, unique=True, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    number_phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    busy_day_id = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey("busy_day.id"), nullable=False, default=1)
    
    busy_day = orm.relationship('BusyDay')


    def __repr__(self):
        return f'<User> {self.name} {self.email}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
