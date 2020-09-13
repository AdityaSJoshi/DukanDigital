from mongoengine import Document, connect
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from flask_mongoengine import MongoEngine
import uuid


from mongoengine import (DateTimeField, StringField, ReferenceField, ListField,
                         FileField, ImageField, EmailField, BooleanField,
                         IntField)

connect(db="DukanDigital", alias='default')

db = MongoEngine()


class BaseDocument(Document):
    created_on = IntField(default=int(datetime.now().timestamp() * 1000))
    modified_on = IntField()
    meta = {
        'indexes': ['created_on', 'modified_on'],
        'allow_inheritance': True,
        'abstract': True,
    }


class USER(BaseDocument):
    user_id = StringField(default=str(uuid.uuid4()))
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    name = StringField(max_length=40)
    shop_name = StringField(max_length=40)
    shop_desc= StringField(max_length=100)

    def __init__(self, email, password, name, shop_name, shop_desc, *args, **kwargs):
        super(USER, self).__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.name = name
        self.shop_name = shop_name
        self.shop_desc = shop_desc
            

 

   


