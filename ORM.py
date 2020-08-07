import datetime

from peewee import chunked, fn

from OrmModel import Person, db
from Request import get_people_from_api
from PersonPrepare import personDataSelector


class ORM:

    def createTable(self):
        db.create_tables([Person])

    def fill_table(self):
        # Because that project does not require CRUD, I've decided to go as easy as I can and
        # clear table before insert data to avoid duplicates.
        self.clear_person_table()

        print("Downloading data from API...")

        # Requesting 1000 records from API ( same package as in file).
        base_persons_from_api = get_people_from_api()

        print("Downloaded!")
        print("Connecting to databse...")

        db.connect()

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
        db.close()

    def clear_person_table(self):
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
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)
        db.close()
        return person_age_list


class SelectMaleAge(SelectAge):
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "male")
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)

        db.close()
        return person_age_list


class SelectFemaleAge(SelectAge):
    def select(self):
        query = Person.select(Person.age).where(Person.gender == "female")
        person_age_list = []
        for age in query:
            person_age_list.append(age.age)

        db.close()
        return person_age_list


class SelectMostPopularCity(Select):
    def __init__(self, limit=5):
        self.limit = limit

    def select(self):
        query = Person.select(fn.Count(Person.city).alias("count"), Person.city).group_by(Person.city).order_by(
            fn.Count(Person.city).desc()).limit(self.limit)

        popular_cities_list = []
        for city in query:
            popular_cities_list.append({"City": city.city, "Count": city.count})

        db.close()
        return popular_cities_list


class SelectMostPopularPassword(Select):
    def __init__(self, limit=5):
        self.limit = limit

    def select(self):
        query = Person.select(fn.Count(Person.password).alias("count"), Person.password).group_by(
            Person.password).order_by(
            fn.Count(Person.password).desc()).limit(self.limit)
        popular_password_list = []
        for password in query:
            popular_password_list.append({"Password": password.password, "Count": password.count})

        db.close()
        return popular_password_list


class SelectPassword(Select):
    def select(self):
        query = Person.select(Person.password)
        password_list = []
        for password in query:
            password_list.append(password.password)
        db.close()
        return password_list


class SelectBirthdayBetween(Select):
    def __init__(self, year_from, month_from, day_from, year_till, month_till, day_till):
        self.day_till = day_till
        self.month_till = month_till
        self.year_till = year_till
        self.day_from = day_from
        self.month_from = month_from
        self.year_from = year_from

    def select(self):
        query = Person.select(Person.dob).where(
            (Person.dob >= datetime.date(int(self.year_from), int(self.month_from), int(self.day_from))) &
            (Person.dob <= datetime.date(int(self.year_till), int(self.month_till), int(self.day_till)))).order_by(
            Person.dob)
        birthday_list = []
        for dob in query:
            birthday_list.append(dob.dob)
        db.close()
        return birthday_list
