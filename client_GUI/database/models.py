from mongoengine import Document, connect
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from flask_mongoengine import MongoEngine
import uuid


from mongoengine import (DateTimeField, StringField, ReferenceField, ListField,
                         FileField, ImageField, EmailField, BooleanField,
                         IntField)
# connect(
#     'app12345678',
#     username='heroku',
#     password='a614e68b445d0d9d1c375740781073b4',
#     host='mongodb://<user>:<password>@alex.mongohq.com:10043/app12345678',
#     port=10043
# )

connect(db="DukanDigital", alias='default', port=27018)

db = MongoEngine()

# def initialize_db(app):
#     db.init_app(app)


class BaseDocument(Document):
    created_on = IntField(default=int(datetime.now().timestamp() * 1000))
    modified_on = IntField()
    meta = {
        'indexes': ['created_on', 'modified_on'],
        'allow_inheritance': True,
        'abstract': True,
    }


class USER(BaseDocument):
    # email = StringField('email',
    #                     validators=[
    #                         InputRequired(),
    #                         Email(message='Invalid email'),
    #                         Length(max=30)
    #                     ])
    # password = PasswordField(
    #     'password', validators=[InputRequired(),
    #                             Length(min=6, max=20)])
    user_id = StringField(default=str(uuid.uuid4()))
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)
    full_name = StringField(max_length=40)
    mobile_no = StringField(min_length=10, max_length=10)
    role = StringField()
    meta = {'indexes': ['email', 'mobile_no', 'user_id'], 'collection': 'users'}

    def __init__(self, email, password, *args, **kwargs):
        super(USER, self).__init__(*args, **kwargs)
        self.email = email


 
 

   


