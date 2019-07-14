from decouple import Config


class AppConfig:
    SECRET_KEY = Config('SECRET')
    MONGO_URI = Config('MONGO_URI')
    DB_NAME = Config('DB_NAME')

