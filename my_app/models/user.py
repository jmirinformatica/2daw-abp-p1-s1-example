from . import db
from flask_login import UserMixin

# Taula users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    # la identificació de l'usuari es basa en el seu email
    def get_id(self):
        return self.email