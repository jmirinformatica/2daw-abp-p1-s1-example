from flask import Flask

def configure_db(app):
    # Inicialitza SQLAlchemy
    from .models import db
    db.init_app(app)
    
    app.logger.info("Database: " + app.config["SQLALCHEMY_DATABASE_URI"])
    app.logger.info("Configuració de la base de dades aplicada")

def create_app():
    app = Flask(__name__)

    # Llegeixo la configuració del config.py de l'arrel
    app.config.from_object('config.Config')

    # Configuració de la base de dades
    configure_db(app)

    with app.app_context():
        from . import routes_main

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)

    app.logger.info("Aplicació iniciada")

    return app