from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class item(FlaskForm):
    username = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    remember_me = BooleanField('Some check mark kinda')
    submit = SubmitField('Add Item')