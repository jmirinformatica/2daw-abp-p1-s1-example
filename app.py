from flask import Flask, redirect, url_for, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Llegeixo la configuració del config.py de l'arrel
app.config.from_object('config.Config')

# the toolbar is only enabled in debug mode
toolbar = DebugToolbarExtension()
toolbar.init_app(app)

@app.route('/')
def init():
    return redirect(url_for('items_list'))

@app.route('/items/list')
def items_list():
    app.logger.info("Es mostra la llista d'items")
    return render_template('items_list.html')
