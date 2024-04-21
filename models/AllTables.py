from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String)
    team_photo = Column(String)
    team_email = Column(String, unique=True)
    team_login = Column(String, unique=True)
    team_password = Column(String)
    users = relationship("Users", back_populates="team")

    __table_args__ = (
        UniqueConstraint('team_email', 'team_login', name='unique_team_login_email'),
    )
class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_photo = Column(String)
    about = Column(String)
    user_email = Column(String)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    team = relationship("Teams", back_populates="users")
