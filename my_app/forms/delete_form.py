from flask_wtf import FlaskForm
from wtforms import SubmitField

# Formulari generic per esborrar i aprofitar la CSRF Protection
class DeleteForm(FlaskForm):
    submit = SubmitField()
