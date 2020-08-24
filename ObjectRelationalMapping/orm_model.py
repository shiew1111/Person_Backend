from peewee import SqliteDatabase, Model, TextField, CharField, DateField, IntegerField

DATABASE = 'persons.db'

# Create a database instance that will manage the connection and
# execute queries
db = SqliteDatabase(DATABASE)


# Create a base-class all our models will inherit, which defines
# the database we'll be using.
class Person(Model):
    uuid = TextField(primary_key=True)
    days_till_birthday = IntegerField()
    age = IntegerField()
    gender = CharField()
    first_name = CharField()
    last_name = CharField()
    dob = DateField()
    phone = CharField()
    cell = CharField()
    password = TextField()
    city = CharField()

    class Meta:
        database = db  # That means Person Model will use persons.db
