from sqlalchemy import create_engine
from models.AllTables import Base
from sqlalchemy.orm import sessionmaker

# Параметры подключения к SQLite
db_url = 'sqlite:///D:/ЫЫЫЫЫЫЫЫЫ/last/Haka_BD.sqlite'

# Параметры подключения к PostgreSQL в Docker
# db_host = "localhost"
# db_port = "5432"  # Стандартный порт для PostgreSQL
# db_name = "main_base"
# db_user = "postgres"
# db_password = "1234"

# Строка подключения к PostgreSQL
# db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url, echo=True)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
