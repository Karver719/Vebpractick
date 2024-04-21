from flask import Flask, request, render_template, redirect, make_response, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from models.sqfunc import add_new_team, add_new_user, getTeam, getUser


# Импортируем необходимые библиотеки и модули.
# Flask - это веб-фреймворк, request - для обработки запросов, render_template - для рендеринга HTML-шаблонов.
# redirect - для перенаправления запросов, make_response - для создания HTTP-ответов.
# os - модуль для работы с операционной системой, secure_filename - функция для безопасности при сохранении файлов.

app = Flask(__name__)
# Создаем экземпляр приложения Flask.

# Путь для сохранения загруженных изображений
UPLOAD_FOLDER = 'uploads/'
# Указываем путь, где будут храниться загруженные файлы.

# Конфигурация для загрузки файлов
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Устанавливаем путь для хранения файлов в конфигурации приложения.

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
# Обрабатывает запросы к корневому маршруту ('/').
# Возвращает HTML-шаблон 'index.html'.

@app.route('/index.html', methods=['GET', 'POST'])
def indreturn():
    return render_template('index.html')
# Маршрут '/index.html' возвращает HTML-шаблон 'index.html'.
# Обработчик аналогичен маршруту '/'.

@app.route('/style.css')
def serve_css():
    try:
        with open('templates/style.css', 'r', encoding='utf-8') as f:
            css = f.read()
        response = make_response(css)
        response.headers['Content-Type'] = 'text/css'
        return response
    except FileNotFoundError:
        return 'File not found', 404
# Обрабатывает запрос к файлу стилей ('/style.css').
# Читает файл 'templates/style.css' и возвращает его содержимое как CSS-файл.

@app.route('/profile.html')
def serve_profile():
    try:
        with open('templates/profile.html', 'r', encoding='utf-8') as f:
            html = f.read()
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'
        return response
    except FileNotFoundError:
        return 'File not found', 404
# Обрабатывает запрос к HTML-файлу ('/profile.html').
# Читает файл 'templates/profile.html' и возвращает его содержимое как HTML-файл.
@app.route('/styleProfile.css')
def serve_style_Profile_css():
    try:
        with open('templates/styleProfile.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        response = make_response(css_content)
        response.headers['Content-Type'] = 'text/css'
        return response
    except FileNotFoundError:
        return 'File not found', 404
@app.route('/img/<filename>', methods=['GET'])
def serve_image(filename):
    # Укажите правильный путь к директории, где находятся изображения
    return send_from_directory('img', filename)

@app.route('/aut.html', methods=['GET'])
def serve_aut():
    try:
        with open('templates/aut.html', 'r', encoding='utf-8') as f:
            html = f.read()
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'
        return response
    except FileNotFoundError:
        return 'File not found', 404
# Обрабатывает запрос к HTML-файлу ('/aut.html').
# Читает файл 'templates/aut.html' и возвращает его содержимое как HTML-файл.
@app.route('/styleAut.css')
def serve_style_Aut_css():
    try:
        with open('templates/styleAut.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        response = make_response(css_content)
        response.headers['Content-Type'] = 'text/css'
        return response
    except FileNotFoundError:
        return 'File not found', 404
@app.route('/autForm', methods=['POST'])
def login():
    # Получаем email и пароль из формы запроса
    email = request.form.get('email')
    password = request.form.get('password')

    team_name, photo, team_email, login, team_password = getTeam(1)

    # Если пользователь найден и пароль совпадает
    if team_name and team_password == password:
        # Перенаправляем пользователя на главную страницу
        return redirect('/')
    else:
        # Возвращаем ошибку 401, если email или пароль неверные
        return 'Неверный email или пароль', 401

# Обрабатывает POST-запрос к '/autForm'.
# Получает email и пароль из формы запроса.
# Печатает email и пароль в консоль.
# Проверяет правильность данных авторизации.
# Если данные правильные, возвращает успех, иначе возвращает ошибку.

@app.route('/regForm', methods=['POST'])
def register():
    # Получаем данные формы
    name = request.form.get('name')
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')
    fio = request.form.get('fio')
    about = request.form.get('about')
    user_email = request.form.get('user_email')

    # Инициализируем путь к файлу по умолчанию
    user_photo = 'img/banner2.jpg'

    # Получаем загруженный файл
    file = request.files.get('photo')

    # Проверяем, был ли файл передан
    if file:
        # Используем secure_filename для обеспечения безопасности имени файла
        filename = secure_filename(file.filename)
        
        # Определяем путь к файлу
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Сохраняем файл в указанном пути
        file.save(photo_path)

        # Заменяем путь к файлу баннера на новый
        user_photo = photo_path
        
    # Добавляем новую команду с использованием данных формы и пути к файлу баннера
    add_new_team(name, user_photo, email, login, password)

    # Добавляем нового пользователя
    # add_new_user(fio, user_photo, about, user_email)

    # Возвращаем успешное сообщение
    return 'Form successfully processed'

@app.route('/addMember', methods=['POST'])
def add_member():
    # Получаем данные из запроса
    fio = request.form.get('fio')
    user_email = request.form.get('user_email')
    about = request.form.get('about')
    user_photo = request.files.get('avatar')

    # Обрабатываем файл аватарки (если передан)
    if user_photo:
        # Используем secure_filename для безопасности файла
        filename = secure_filename(user_photo.filename)
        # Сохраняем файл
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        user_photo.save(photo_path)
    else:
        # Если файл аватарки не передан, используем путь по умолчанию
        photo_path = 'img/banner.png'
    
    # Вызываем функцию для добавления нового пользователя в базу данных
    add_new_user(fio, photo_path, about, user_email)

    # Возвращаем успешное сообщение
    return 'Участник успешно добавлен'


# Обрабатывает POST-запрос к '/regForm'.
# Получает данные из формы запроса: имя, email, логин, пароль и др.
# Получает файл изображения, если он был загружен.
# Выводит данные формы в консоль.
# Если изображение было загружено, сохраняет его в указанную папку.
# Возвращает успешное сообщение.

@app.route('/registr.html')
def serve_reg():
    try:
        with open('templates/registr.html', 'r', encoding='utf-8') as f:
            html = f.read()
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'
        return response
    except FileNotFoundError:
        return 'File not found', 404
# Обрабатывает запрос к HTML-файлу ('/registr.html').
# Читает файл 'templates/registr.html' и возвращает его содержимое как HTML-файл.

@app.route('/styleReg.css')
def serve_style_reg_css():
    try:
        # Открываем файл styleReg.css из папки templates
        with open('templates/styleReg.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Создаем ответ с содержимым файла
        response = make_response(css_content)
        
        # Устанавливаем заголовок контента как text/css
        response.headers['Content-Type'] = 'text/css'
        
        return response
    except FileNotFoundError:
        # Возвращаем ошибку 404, если файл не найден
        return 'File not found', 404


if __name__ == '__main__':
    app.run()
# Запускает приложение Flask на локальном сервере.
