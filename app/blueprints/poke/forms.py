from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    img_url = StringField('Image URL', validators=[DataRequired()])
    poke_name = StringField('Poke Name', validators=[DataRequired()])
    ability = StringField('Ability', validators=[DataRequired()])
    base_experience = IntegerField('Base Experience', validators=[DataRequired()])
    hp = IntegerField('HP', validators=[DataRequired()])
    attack = IntegerField('Attack', validators=[DataRequired()])
    defense = IntegerField('Defense', validators=[DataRequired()])
    submit = SubmitField('Create Pokemon')
