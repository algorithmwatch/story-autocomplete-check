from peewee import *
import datetime

db = SqliteDatabase('suggestions.db')

class Suggestion(Model):
    concept = CharField()
    phrase = CharField()
    suggestion = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    country_IP = CharField()
    language = CharField()
    service = CharField()

    class Meta:
        database = db

db.connect()

db.create_tables([Suggestion], safe = True)