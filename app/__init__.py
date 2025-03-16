from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Set up SQLite database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Import blueprints only after app and db are initialized
    from app.routes import main
    app.register_blueprint(main)

    # Ensure the database and tables exist
    with app.app_context():
        if not os.path.exists('instance/app.db'):
            db.create_all()

    return app
