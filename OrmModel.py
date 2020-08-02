from peewee import *

DATABASE = 'persons.db'

# Create a database instance that will manage the connection and
# execute queries
db = SqliteDatabase(DATABASE)


# Create a base-class all our models will inherit, which defines
# the database we'll be using.
class Person(Model):
    daysTillBirthday = IntegerField()
    gender = CharField()
    first_name = CharField()
    last_name = CharField()
    dob = DateField()
    phone = IntegerField()
    cell = IntegerField()
    password = TextField()
    city = CharField()

    class Meta:
        database = db  # That means Person Model will use persons.db
# db.create_tables([Person])
# Person(gender="male",
#        first_name="Tim",
#        last_name="Dupa",
#        dob="1997-11-01",
#        phone="0775957264",
#        cell="0753022945",
#        password="loki",
#        city="Bjerka").save()

# dupa = Person.select().where(Person.gender == 'male').get()
#
# print(dupa.last_name)
# dupa.last_name = "dupaV2"
# print(dupa.last_name)
# db.close()
