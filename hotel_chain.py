from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def regestranion():
    if request.method == 'GET':
        return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <title>Бронирование номера в гостинице</title>
</head>
<body>
<h1 align="center">Сервис бронирования гостиниц в Москве</h1>
<h2 align="center">Войдите или зарегестрируйтесь</h2>
<div class="container">
    <form class="login_form" method="post">
        <div class="form-group">
            <p style="margin-left: 70px;"></p>
            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name" required>
            <p style="margin-left: 40px;"></p>
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                   placeholder="Введите адрес электронной почты" name="email" required>
            <p style="margin-left: 40px;"></p>
            <input type="text" class="form-control" id="password" placeholder="Введите пароль" name="password" required>
            <p style="margin-left: 40px;"></p>
        </div>
        <p style="margin-left: 40px;"></p>
        <button type="submit" class="btn btn-primary">Вход/Регестрация</button>
    </form>
</div>
</body>
</html>"""
    elif request.method == 'POST':
        return redirect('/map')


@app.route('/map', methods=['POST', 'GET'])
def hotels_map():
    if request.method == 'GET':
        return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Сервис бронирования гостиниц в Москве</h1>
<h2 align="center">Выберете гостиницу на карте и укажите ее адрес</h2>
<div class="container">
    <form class="login_form" method="post">
        <div class="form-group">
            <script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa49dff812320aa6f55a4f5210ed0aaa131d03b15140050b3c5720dc3260357e7&amp;width=500&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>
            <label for="educationSelect"></label>
            <select class="form-control" id="educationSelect" name="education">
                <option>ул. Грузинский Вал, 26, стр. 1, Москва</option>
                <option>ул. Новый Арбат, 26, Москва</option>
                <option>Смоленская ул., 10, Москва</option>
                <option>Нижегородская ул., 12, Москва</option>
                <option>Мерзляковский пер., 10, Москва</option>
                <option>Шепелюгинская ул., 5, корп. 1, Москва</option>
                <option>ул. Чаянова, 18А, Москва</option>
                <option>Москва, Проектируемый проезд № 6518</option>
                <option>3-я Сокольническая ул., 4, Москва</option>
                <option>Тверская ул., 17, Москва</option>
            </select>
        </div>
        <p style="margin-left: 40px;"></p>
        <button type="submit" class="btn btn-primary">Подтвердить</button>
    </form>
</div>
</body>
</html>"""
    elif request.method == 'POST':
        return redirect('/dt')


@app.route('/dt', methods=['POST', 'GET'])
def date_and_time():
    if request.method == 'GET':
        return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Сервис бронирования гостиниц в Москве</h1>
<h2 align="center">Выберете дату, время начала и конца бронирования</h2>
<div class="container">
    <form class="login_form" method="post">
        <div class="form-group">
            <p style="margin-left: 70px;"></p>
            <label for="educationSelect"> Выберите дату и время начала </label>
            <input type="datetime-local" id="datetimeLocalToday">
            <script>
            document.getElementById('datetimeLocalToday').value = new Date().toJSON().slice(0,0);
            </script>
            <p style="margin-left: 40px;"></p>
            <label for="educationSelect"> Выберите дату и время конца  </label>
            <input type="datetime-local" id="datetimeLocalToday">
            <script>
            document1.getElementById('datetimeLocalToday').value = new Date().toJSON().slice(0,0);
            </script>
            <p style="margin-left: 40px;"></p>
        </div>
        <button type="submit" class="btn btn-primary">Подтвердить</button>
    </form>
</div>
</body>
</html>"""
    elif request.method == 'POST':
        return "Бронь успешно создана"


if __name__ == '__main__':
    app.run(port=8080, host="")