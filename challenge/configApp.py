from datetime import datetime
from sqlalchemy.pool import QueuePool
from flask import Flask, request, g
from dotenv import load_dotenv
from config.errorHandler import register_error_handlers
from config.InterceptRequestMiddleware import InterceptRequestMiddleware
from flask_cors import CORS
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

ENVS = {"local":".env","dev": "dev.env","homo": "homo.env","prod": "prod.env"}

def gunicorn_execution(env):
    if env not in ENVS:
        exit("Please specify a valid environment : local, dev, homo, prod")
    load_dotenv(ENVS[env])
        
def python_execution():
    if len(sys.argv) == 2 and sys.argv[1] in ENVS:
        load_dotenv(ENVS[sys.argv[1]])
    else:
        exit("Please specify a valid environment : local, dev, homo, prod")

def create_app(env=None):
    entorno = None
    if env==None:
        python_execution()
    else:
        gunicorn_execution(env)
    if env != None:
        entorno = env
    else:
        entorno = sys.argv[1]
    from register import api

    DBENV= None
    if entorno =="local":
        LOCAL = f'localhost:{os.getenv("POSTGRES_PORT")}'
        DBENV=LOCAL
    else:
        DOCKER = f'postgres:{os.getenv("POSTGRES_PORT")}'
        DBENV=DOCKER

    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.wsgi_app = InterceptRequestMiddleware(app.wsgi_app)
    db_url = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{DBENV}/storicardchallenge'

    engine = create_engine(db_url, poolclass=QueuePool, pool_size=5, pool_recycle=3600, max_overflow=5)
    app.dbengine = engine
    app.db = sessionmaker(bind=engine)
    CORS(app, resources={r"/*": {"origins": "*"}})
    api.init_app(app)
    app.url_map.strict_slashes = False

    @app.before_request
    def before_request():

        g.uidRequest = request.environ['HTTP_X_REQUEST_ID']
        g.httpNow = request.environ['HTTP_DATE']
        g.entorno = entorno
        
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, X-API-KEY')
        g.uidRequest = request.environ['HTTP_X_REQUEST_ID']
        g.httpNow = request.environ['HTTP_DATE']
        response_time_now = datetime.now()
        duration = (response_time_now - g.httpNow).total_seconds()
        print(duration)
        if response.json == None:
            return response

        return response

    register_error_handlers(app)
    return app

def get_db_session(app):
    Session = app.db
    new_session= Session()
    return new_session

