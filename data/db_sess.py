import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec


SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = 'sqlite:///' + db_file.strip()
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)
    session = create_session()
    from data.hotels import Hotel
    if session.query(Hotel).count() == 0:
        print('Сервис запущен, происходит загрузка первичных данных.')
        session.close()
        start_data_in_bd()  # добавление в БД информацию
    else:
        print('сервис доступен.')
        session.close()


def start_data_in_bd():
    session = create_session()
    from data.hotels import Hotel
    from data.users import User
    from data.busy_days import BusyDay
    hotel_file = open('data/hotels.csv')
    for htl in hotel_file.readlines():
        hotel = Hotel()
        data = htl.split(';')
        hotel.id = int(data[0])
        hotel.coordinate = str(data[1])
        session.add(hotel)
        print(hotel)
    hotel_file.close()
    user_file = open('data/users.csv')
    for nxt_usr in user_file.readlines():
        user = User()
        data = nxt_usr.split(';')
        user.id = int(data[0])
        user.name = str(data[1])
        user.email = str(data[2])
        user.about = str(data[3])
        user.number_phone = int(data[4])
        user.set_password(data[5])
        user.busy_day_id = int(data[6])
        session.add(user)
        print(user)
    user_file.close()
    busy_day_file = open('data/busy_days.csv')
    for b_d in busy_day_file.readlines():
        busy_day = BusyDay()
        data = b_d.split(';')
        busy_day.id = int(data[0])
        busy_day.arrive_day = int(data[1])
        busy_day.departure_day = int(data[2])
        busy_day.hotel_id = int(data[3])
        session.add(busy_day)
        print(busy_day)
    busy_day_file.close()
    session.commit()
    session.close()


def new_bron_in_bd(bron):
    session = create_session()
    session.add(bron)
    print(bron)
    session.commit()
    session.close()


def bron_del_from_db(id):
    from data.busy_days import BusyDay
    session = create_session()
    try:
        busy_day = session.query(BusyDay).filter_by(id=id).one()
        session.delete(busy_day)
        session.commit()
        print('Busy day id = {id} is deleted from the database')
    except sa.exc.NoResultFound:  # sqlalchemy.exc.NoResultFound
        print('Busy day id {id} absent in the database')
    session.close()


def new_user(user):
    session = create_session()
    session.add(user)
    print(user)
    session.commit()
    session.close()


def create_session() -> Session:
    global __factory
    return __factory()
