from . import db

# Taula stores
class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    # relacions
    items = db.relationship("Item", backref="store")