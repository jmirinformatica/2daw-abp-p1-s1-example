from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    msg = TextAreaField(
        validators=[ DataRequired()]
    )
    submit = SubmitField()