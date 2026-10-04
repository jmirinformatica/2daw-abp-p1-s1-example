from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    # clau secreta per a les sessions guardades a les cookies
    SECRET_KEY = environ.get('SECRET_KEY')

    # debug toolbar
    # https://stackoverflow.com/questions/63116419/evaluate-boolean-environment-variable-in-python
    DEBUG_TB_ENABLED = environ.get('DEBUG_TB_ENABLED', "false").lower() == "true"

    # paràmetre que farà servir SQLAlchemy per a connectar-se
    default_db = "sqlite:///" + basedir + "/sqlite/database.db"
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI', default_db)

    # mostre als logs les ordres SQL que s'executen
    SQLALCHEMY_ECHO = environ.get('DEBUG_TB_ENABLED', "true").lower() == "true"
