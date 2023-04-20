from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])  # Начальная страница
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
    <h2 align="center">Войдите или зарегистрируйтесь</h2>
    
    <div class="container">
        <h4>Войдите в свой аккаунт</h4>
        
        <form action="/entrance" method="get" target="_blank">
        <button type="submit">Вход</button>
        <! - - Кнопка перехода на страницу входа -->

        </form>
        
        <br>
        <h4>Или</h4>
        <br>
        <h4>Зарегистрируйтесь, если его нет</h4>
        
        <form action="/reg" method="get" target="_blank">
        <button type="submit">Регистрация</button>
        <! - - Кнопка перехода на страницу регестрации -->
        </form>
    </div>
    </body>
    </html>"""


@app.route('/entrance', methods=['POST', 'GET'])  # Страница входа
def vhod():
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
            <title>Вход</title>
        </head>
        
        <body>
        <h1 align="center">Вход</h1>
        
        <div class="container">
            <form class="login_form" method="post">
                <div class="form-group">
                
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                        placeholder="Введите адрес эл. почты" name="email" required>
                    <! - - Окно ввода эл почты -->

                    <br>

                    <input type="password" class="form-control" id="password" aria-describedby="passwordHelp"
                        placeholder="Введите пароль" name="password" required>
                    <! - - Окно ввода эл почты -->

                    <br>
                    
                </div>
                
                <button type="submit" class="btn btn-primary">Войти</button>
                <! - - Кнопка перехода в личный кабинет -->

            </form>
        </div>
        </body>
        </html>"""
    elif request.method == 'POST':
        return redirect('/cabin')


@app.route('/reg', methods=['POST', 'GET'])  # Страница регестрации
def reg():
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
            <title>Регистрация</title>
        </head>
        
        <body>
        <h1 align="center">Регистрация</h1>
        
        <div class="container">
            <form class="login_form" method="post">
                <div class="form-group">
                
                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию"
                        name="surname" required>
                    <! - - Окно ввода Фамилии -->
                    
                    <br>
                    
                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name" required>
                    <! - - Окно ввода Имени -->
                    
                    <br>
                </div>
                
                <div class="form-group">
                
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                        placeholder="Введите адрес почты" name="email" required>
                    <! - - Окно ввода эл почты -->
                    
                    <br>
                    
                    <input type="phonenumber" class="form-control" id="phonenumber" aria-describedby="phonenumberHelp"
                        placeholder="Введите номер телефона" name="phonenumber" required>
                    <! - - Окно ввода номера телефона -->
                    
                    <br>
                    
                    <input type="password" class="form-control" id="password" aria-describedby="passwordHelp"
                        placeholder="Введите пароль" name="password" required>
                    <! - - Окно ввода пароля -->
                    
                    <br>
                    
                </div>
                
                <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                <! - - Кнопка перехода в личный кабинет -->
            </form>
        </div>
        </body>
        </html>"""
    elif request.method == 'POST':
        return redirect('/cabin')


@app.route('/cabin', methods=['POST', 'GET'])  # Страница личного кабинета
def cab():
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
            <title>Личный кабинет</title>
        </head>
        
        <body>
        <h1 align="center">Личный кабинет</h1>
        
        <div class="container">
        
        <! - - Здесь нужно выводить из базы данных -->
        <h3>Личная информация:</h3>
        <h5>Имя:</h5>
        <h5>Фамилия:</h5>
        <h5>Эл. почта:</h5>
        <h5>Номер телефона:</h5>
        <h5>Пароль:</h5>
        
        <form action="/reg" method="get" target="_blank">
        
        <button type="submit">Заполнить заново</button>
        <! - - Кнопка перехода для регестрации заново. Здесь нужно удалять данные о пользователе из базы данных -->
        
        </form>
        
        <hr>
        
        <h3>Действующие брони:</h3>
        <! - - Здесь нужно выводить из базы данных -->

        <hr>
        
            <form class="login_form" method="post">
                <button type="submit" class="btn btn-primary">Создать новую бронь</button>
                <! - - Кнопка перехода на выбор отеля по карте -->
            </form>
        </div>
        </body>
        </html>"""
    elif request.method == 'POST':
        return redirect('/map')


@app.route('/map', methods=['POST', 'GET'])  # Страница выбора адреса
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
            <title>Выбор места</title>
        </head>
        
        <body>
        
        <h1 align="center">Сервис бронирования гостиниц в Москве</h1>
        <h2 align="center">Выберете гостиницу на карте и укажите ее адрес</h2>
        
        <div class="container">
            <form class="login_form" method="post">
                <div class="form-group">
                
                    <script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa49dff812320aa6f55a4f5210ed0aaa131d03b15140050b3c5720dc3260357e7&amp;width=500&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>
                    <! - - Вывод карты -->
                    
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
                    <! - - Окно выбора адреса, его нужно записывать в бд -->
                    
                </div>
                <p style="margin-left: 40px;"></p>
                
                <button type="submit" class="btn btn-primary">Подтвердить</button>
                <! - - Кнопка перехода к выбору даты и времени -->
                
            </form>
        </div>
        </body>
        </html>"""
    elif request.method == 'POST':
        return redirect('/dt')


@app.route('/dt', methods=['POST', 'GET'])  # Страница выбора даты и времени
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
            <title>Выбор времени</title>
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
                    <! - - Выбор даты и времени начала, его нужно передовать в бд -->
                    
                    <p style="margin-left: 40px;"></p>
                    <label for="educationSelect"> Выберите дату и время конца  </label>
                    
                    <input type="datetime-local" id="datetimeLocalToday">
                    <script>
                    document1.getElementById('datetimeLocalToday').value = new Date().toJSON().slice(0,0);
                    </script>
                    <! - - Выбор даты и времени начала, его нужно передовать в бд -->
                    
                    <p style="margin-left: 40px;"></p>
                </div>
                <button type="submit" class="btn btn-primary">Подтвердить</button>
                <! - - Кнопка подтверждения нового бронирования -->
            </form>
        </div>
        </body>
        </html>"""
    elif request.method == 'POST':
        return "Бронь успешно создана"
        # Здесь добавлю конечное окно


if __name__ == '__main__':
    app.run(port=8080, host="")
