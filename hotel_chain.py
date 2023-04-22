from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)


class FormsClass:
    pass  # пока один класс для всех функций, тк с каждой разное взаимодействие
            # Ты можешь создать сколько нужно для каждой функции


@app.route('/', methods=['GET'])  # Начальная страница
def regestranion():
    form = FormsClass()
    return render_template('start_page.html', form=form)


@app.route('/entrance', methods=['POST', 'GET'])  # Страница входа
def vhod():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('entrance_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/cabin')


@app.route('/reg', methods=['POST', 'GET'])  # Страница регестрации
def reg():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('regestr_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/cabin')


@app.route('/cabin', methods=['POST', 'GET'])  # Страница личного кабинета
def cab():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('profil_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/dt')


@app.route('/dt', methods=['POST', 'GET'])  # Страница выбора даты и времени
def date_and_time():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('date_time_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/map')


@app.route('/map', methods=['POST', 'GET'])  # Страница выбора адреса
def hotels_map():
    form = FormsClass()
    if request.method == 'GET':
        return render_template('map_page.html', form=form)
    elif request.method == 'POST':
        return redirect('/closereg')


@app.route('/closereg', methods=['GET'])  # Страница завершения регестрации и перенаправление в личный кабинет
def close_reg():
    form = FormsClass()
    return render_template('close_reg_page.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host="")
