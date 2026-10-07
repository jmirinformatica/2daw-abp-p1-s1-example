from my_app.helper_role import Role

from . import db
from flask_login import UserMixin

# Taula users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def is_editor(self):
        return self.role == Role.editor

    # la identificació de l'usuari es basa en el seu email
    def get_id(self):
        return self.email