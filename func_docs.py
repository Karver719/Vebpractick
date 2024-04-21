from models.sqfunc import add_new_team, add_new_user, getTeam, getUser

#   Создание новой команды:
#add_new_team(имя команды, банер, почта команды, логин команды, пароль команды)

# name = "Асист-камазист"
# photo = "img.jpg"
# email = "bibki@mail.ru"
# login = "BigJopa"
# password = "I2f59"
# add_new_team(name, photo, email, login, password)

#   Создание нового участника:
# fio = "Иванов Иван Иванович"
# user_photo = "photo1.jpg"
# about = ""
# u_email = "EEEEva@gmail.com"
# add_new_user(fio, user_photo, about, u_email)

print( getTeam(1) )

print( getUser(1) )
