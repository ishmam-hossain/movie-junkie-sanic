from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Sanic
from sanic_cors import CORS
from simple_bcrypt import Bcrypt
from .config import AppConfig
from .auth import auth_bp

app = Sanic(__name__)
bcrypt = Bcrypt(app)
CORS(app)

app.config.from_object(AppConfig)
db = None


@app.listener('before_server_start')
def initializer(sanic, loop):
    global db
    # from motor.motor_asyncio import AsyncIOMotorClient
    from pymongo import MongoClient
    mongo_uri = app.config.get('SECRET')
    db_name = app.config.get('DB_NAME')

    # db = MongoClient(mongo_uri).test_mongo_ishmam
    db = AsyncIOMotorClient(mongo_uri).test_mongo_ishmam


app.blueprint(auth_bp)




