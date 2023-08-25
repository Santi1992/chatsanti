from flask import current_app

def get_db_session():
    Session = current_app.db
    new_session= Session()
    return new_session

def connection_avialable():
    engine = current_app.dbengine
    pool = engine.pool
    print("Conexiones en uso:", pool.checkedout())
    print("Conexiones disponibles:", pool.checkedin())
