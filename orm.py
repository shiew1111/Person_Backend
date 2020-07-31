from peewee import *

DATABASE = 'persons.db'

# Create a database instance that will manage the connection and
# execute queries
database = SqliteDatabase(DATABASE)


# Create a base-class all our models will inherit, which defines
# the database we'll be using.
class Person(Model):
    gender = CharField()
    first_name = CharField()
    last_name = CharField()
    dob = DateField()
    phone = IntegerField()
    cell = IntegerField()
    password = TextField()
    city = CharField()

    class Meta:
        database = database
