import datetime

from peewee import *

from OrmModel import Person, db
from Request import Request
from PersonPrepare import personDataSelector


class ORM:

    def createTable(self):
        db.create_tables([Person])

    def fillTable(self):
        # Because that project does not require CRUD, I've decided to go as easy as I can and
        # clear table before insert data to avoid duplicates.
        self.ClearPersonTable()

        print("Downloading data from API...")

        # Requesting 1000 records from API ( same package as in file).
        basePersonsFromAPI = Request().from_api()

        print("Downloaded!")
        print("Connecting to databse...")

        db.connect()

        print("Connected!")
        print("Saving processed records into database...")

        PersonPreparedList = []
        with db.atomic():
            # With for loop take all results from API and prepare every row to be matching with database.
            for person in basePersonsFromAPI:
                # Preparing single row.
                PersonPrepared = personDataSelector(person)
                # Saving prepared row into list.
                PersonPreparedList.append(PersonPrepared)
            # Cutting records into chunks,
            # because SQLite limit of variables per query.
            for batch in chunked(PersonPreparedList, 90):
                # Executing 99 rows from list.
                Person.insert_many(batch).execute()

        print("Records saved! Closing database connection!")
        db.close()

    def ClearPersonTable(self):
        db.connect()
        query = Person.delete()
        query.execute()
        db.close()


class Select:
    def select(self):
        query = Person.select()
        db.close()
        return query


class SelectMale(Select):
    def select(self):
        query = Person.select(Person.gender).where(Person.gender == "male")
        db.close()
        return query


class SelectFemale(Select):
    def select(self):
        query = Person.select(Person.gender).where(Person.gender == "female")
        db.close()
        return query


class SelectAge(Select):
    def select(self):
        query = Person.select(Person.age)
        db.close()
        return query


class SelectMaleAge(SelectAge):
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "male")
        db.close()
        return query


class SelectFemaleAge(SelectAge):
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "female")
        db.close()
        return query


class SelectMostPopularCity(Select):
    def select(self, limit=5):
        query = Person.select(fn.Count(Person.city).alias("count"), Person.city).group_by(Person.city).order_by(
            fn.Count(Person.city).desc()).limit(limit)
        db.close()
        return query


class SelectMostPopularPassword(Select):
    def select(self, limit=5):
        query = Person.select(fn.Count(Person.password).alias("count"), Person.password).group_by(
            Person.password).order_by(
            fn.Count(Person.password).desc()).limit(limit)
        db.close()
        return query


class SelectLongPassword(Select):
    def select(self, ):
        query = Person.select(Person.password).where(fn.LENGTH(Person.password) >= 8)
        db.close()
        return query


class SelectBirthdayBetween(Select):
    def __init__(self, startYear, startMonth, startDay, tillYear, tillMonth, tillDay):
        self.startYear = startYear
        self.startMonth = startMonth
        self.startDay = startDay
        self.tillYear = tillYear
        self.tillMonth = tillMonth
        self.tillDay = tillDay

    def select(self):
        query = Person.select(Person.dob).where(
            (Person.dob >= datetime.date(int(self.startYear), int(self.startMonth), int(self.startDay))) &
            (Person.dob <= datetime.date(int(self.tillYear), int(self.tillMonth), int(self.tillDay)))).order_by(
            Person.dob)
        db.close()
        return query


