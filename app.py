from flask import Flask, redirect, url_for, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
import os

from models import db
from models.item import Item
from models.store import Store

app = Flask(__name__)

# Llegeixo la configuració del config.py de l'arrel
app.config.from_object('config.Config')

# the toolbar is only enabled in debug mode
toolbar = DebugToolbarExtension()
toolbar.init_app(app)

# Inicio SQLAlchemy
db.init_app(app)

# Defineixo rutes
@app.route('/')
def init():
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    # select amb join que retorna una llista dwe resultats
    items_with_stores = db.session.query(Item, Store).join(Store).order_by(Item.id.asc()).all()
    # depuració
    count = len(items_with_stores)
    app.logger.info(f"Hi ha {count} items a la BD")
    # missatges flash
    flash(f"Hi ha {count} items disponibles", "info")
    # mostrar pàgina
    return render_template('items_list.html', items_with_stores = items_with_stores)

@app.route('/items/read/<int:item_id>')
def items_read(item_id):
    # select amb join i 1 resultat
    (item, store) = db.session.query(Item, Store).join(Store).filter(Item.id == item_id).one()
    
    return render_template('items_read.html', item = item, store = store)
