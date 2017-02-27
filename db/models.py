from peewee import *

db = SqliteDatabase('database.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


def create_tables():
    if not Person.table_exists():
        db.create_tables([Person])