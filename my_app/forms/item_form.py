from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class ItemForm(FlaskForm):
    nom = StringField(
        validators = [DataRequired()]
    )
    unitats = IntegerField(
        validators = [DataRequired(), NumberRange(min=1)]
    )
    store_id = SelectField(
        validators = [InputRequired()]
    )
    submit = SubmitField()