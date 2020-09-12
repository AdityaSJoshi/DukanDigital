from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField,TextAreaField
from wtforms.validators import DataRequired, NumberRange

class item(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price',validators=[DataRequired(),NumberRange(min=0, max=1000000)])
    #remember_me = BooleanField('Some check mark kinda')
    submit = SubmitField('Add Item')

class item(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price',validators=[DataRequired(),NumberRange(min=0, max=1000000)])
    #remember_me = BooleanField('Some check mark kinda')
    submit = SubmitField('Add Item')