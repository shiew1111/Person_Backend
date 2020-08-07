import datetime
import sys
from peewee import chunked, fn, OperationalError

from OrmModel import Person, db
from Request import get_people_from_api
from PersonPrepare import personDataSelector


class ORM:
    @db.connection_context()
    def create_table(self):
        db.create_tables([Person])
        print("Created table person.")

    @db.connection_context()
    def fill_table(self):
        try:

            # Because that project does not require CRUD, I've decided to go as easy as I can and
            # clear table before insert data to avoid duplicates.
            self.clear_person_table()

            print("Downloading data from API...")

            # Requesting 1000 records from API ( same package as in file).
            base_persons_from_api = get_people_from_api()

            print("Downloaded!")
            print("Connecting to databse...")

            print("Connected!")
            print("Saving processed records into database...")

            person_prepared_list = []
            with db.atomic():
                # With for loop take all results from API and prepare every row to be matching with database.
                for person in base_persons_from_api:
                    # Preparing single row.
                    person_prepared = personDataSelector(person)
                    # Saving prepared row into list.
                    person_prepared_list.append(person_prepared)
                # Cutting records into chunks,
                # because SQLite limit of variables per query.
                for batch in chunked(person_prepared_list, 90):
                    # Executing 90 rows from list.
                    Person.insert_many(batch).execute()

            print("Records saved! Closing database connection!")
        except OperationalError as e:
            if e.args == ('no such table: person',):
                print("OperationalError: Table person not found. Try UI.py --create_table")
                sys.exit(1)

    @db.connection_context()
    def clear_person_table(self):
        try:
            query = Person.delete()
            query.execute()
        except OperationalError as e:
            if e.args == ('no such table: person',):
                print("OperationalError:Table person not found. Try UI.py --create_table")
                sys.exit(1)


class Select:
    @db.connection_context()
    def select(self):
        query = Person.select()

        return query


class SelectMale(Select):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.gender).where(Person.gender == "male")

        return query


class SelectFemale(Select):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.gender).where(Person.gender == "female")

        return query


class SelectAge(Select):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.age)
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)

        return person_age_list


class SelectMaleAge(SelectAge):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "male")
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)

        return person_age_list


class SelectFemaleAge(SelectAge):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "female")
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)

        return person_age_list


class SelectMostPopularCity(Select):
    def __init__(self, limit=5):
        self.limit = limit

    @db.connection_context()
    def select(self):
        query = Person.select(fn.Count(Person.city).alias("count"), Person.city).group_by(Person.city).order_by(
            fn.Count(Person.city).desc()).limit(self.limit)

        popular_cities_list = []
        for city in query:
            popular_cities_list.append({"City": city.city, "Count": city.count})

        return popular_cities_list


class SelectMostPopularPassword(Select):
    def __init__(self, limit=5):
        self.limit = limit

    @db.connection_context()
    def select(self):
        query = Person.select(fn.Count(Person.password).alias("count"), Person.password).group_by(
            Person.password).order_by(
            fn.Count(Person.password).desc()).limit(self.limit)
        popular_password_list = []
        for password in query:
            popular_password_list.append({"Password": password.password, "Count": password.count})

        return popular_password_list


class SelectPassword(Select):
    @db.connection_context()
    def select(self):
        query = Person.select(Person.password)
        password_list = []
        for password in query:
            password_list.append(password.password)

        return password_list


class SelectBirthdayBetween(Select):
    def __init__(self, year_from, month_from, day_from, year_till, month_till, day_till):
        self.day_till = day_till
        self.month_till = month_till
        self.year_till = year_till
        self.day_from = day_from
        self.month_from = month_from
        self.year_from = year_from

    @db.connection_context()
    def select(self):
        query = Person.select(Person.dob).where(
            (Person.dob >= datetime.date(int(self.year_from), int(self.month_from), int(self.day_from))) &
            (Person.dob <= datetime.date(int(self.year_till), int(self.month_till), int(self.day_till)))).order_by(
            Person.dob)
        birthday_list = []
        for dob in query:
            birthday_list.append(dob.dob)

        return birthday_list



