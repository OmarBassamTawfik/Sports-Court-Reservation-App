import psycopg2
import psycopg2.extras
from flask import current_app, g
from datetime import datetime

# Define the PostgreSQL connection string (Neon)
DATABASE_URI = "postgresql://sport%20court%20reservation_owner:cYoU2qvJO7Gz@ep-yellow-thunder-a2egfzro.eu-central-1.aws.neon.tech/sport%20court%20reservation?sslmode=require"

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(DATABASE_URI)
        g.db.cursor_factory = psycopg2.extras.DictCursor
        g.db.set_session(autocommit=True, timezone='UTC')  
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
