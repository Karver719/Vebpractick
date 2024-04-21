from dataBase import Session
from models.AllTables import Teams, Users

session = Session()

def add_new_team(team_name, team_photo, team_email, team_login, team_password):
    new_team = Teams(team_name=team_name, team_photo=team_photo, team_email=team_email,
                         team_login=team_login, team_password=team_password)
    session.add(new_team)
    session.commit()
    print("Новая команда добавлена.")
    session.close()

def add_new_user(user_name, user_photo, about, user_email):
    new_user = Users(user_name=user_name, user_photo=user_photo, about=about,
                         user_email=user_email)
    session.add(new_user)
    session.commit()
    print("Новый участник добавлен.")
    session.close()

def getTeam(team_id):
    team = session.query(Teams).filter_by(team_id=team_id).first()
    # Выводим данные комманды
    if team:
        return [team.team_name, team.team_photo, team.team_email, team.team_login, team.team_password]

def getUser(user_id):
    user = session.query(Users).filter_by(user_id=user_id).first()

    # Выводим данные пользователя
    if user:
        return [user.user_name, user.user_photo, user.about, user.user_email]

#=======================================================