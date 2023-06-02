from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon', validators=[DataRequired()])
    submit = SubmitField('Submit')


