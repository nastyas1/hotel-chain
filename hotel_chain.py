from flask import Flask, url_for, request, redirect, render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_login import LoginManager
from data.db_sess import *
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_sess
from wtforms.fields import DateField, TimeField, DateTimeField, SelectField
from datetime import datetime, date



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from data.users import User
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    number_phone = StringField('Number phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    about = StringField('About', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
    
class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    enddate = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')
 




class FormsClass:
    pass  # пока один класс для всех функций, тк с каждой разное взаимодействие
            # Ты можешь создать сколько нужно для каждой функции


@app.route('/', methods=['GET'])  # Начальная страница
def regestranion():
    form = FormsClass()
    return render_template('start_page.html', form=form)


# @app.route('/entrance', methods=['POST', 'GET'])  # Страница входа
# def vhod():
#     form = FormsClass()
#     if request.method == 'GET':
#         return render_template('entrance_page.html', form=form)
#     elif request.method == 'POST':

#         return redirect('/cabin')


@app.route('/login', methods=['GET', 'POST'])
def login():
    from data.users import User
    form = LoginForm()
    # if form.validate_on_submit():
    if request.method == 'POST':
        db_sess = create_session()
        user = db_sess.query(User).filter(User.name == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/cabin")
        return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)



@app.route('/reg', methods=['POST', 'GET'])  # Страница регистрации
def reg():
    form = LoginForm()
    if form.validate_on_submit():
        from data.users import User
        from data.db_sess import new_user
        user = User()
        user.name = form.username.data
        user.email = form.email.data
        user.about = form.email.data
        user.number_phone = form.number_phone.data
        user.hashed_password = form.password.data
        new_user(user)
        return redirect('/cabin')
    return render_template('reg.html', form=form)


@app.route('/cabin', methods=['POST', 'GET'])  # Страница личного кабинета
def cab():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('profil_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/dt')



@app.route('/dt', methods=['POST', 'GET'])  # Страница выбора даты и времени
def date_and_time():
    form = InfoForm()
    if form.validate_on_submit():
        from data.busy_days import BusyDay
        from data.db_sess import new_bron_in_bd
        busy_day = BusyDay()
        st = form.startdate.data # дата начала
        st_day = st - date(day=1, month=1, year=st.year)
        busy_day.arrive_day = int(st_day.days)
        en = form.enddate.data # дата конца
        en_day = en - date(day=1, month=1, year=en.year)
        busy_day.departure_day = int(en_day.days)
        new_bron_in_bd(busy_day)
        return redirect('/map')
    return render_template('date_time_page.html', form=form)


@app.route('/map', methods=['POST', 'GET'])  # Страница выбора адреса
def hotels_map():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('map_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/closereg')


@app.route('/closereg', methods=['GET'])  # Страница завершения регистрации и перенаправление в личный кабинет
def close_reg():
    form = FormsClass()
    return render_template('close_reg_page.html', form=form)


def main():
    app.run(port=8080, host='')
