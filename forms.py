from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired('Please enter your name')])
    submit = SubmitField('Submit')