from peewee import chunked

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
            for batch in chunked(PersonPreparedList, 99):
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
        db.connect()
        query = Person.select()
        db.close()
        return query


class SelectMale(Select):
    def selectMale(self):
        query = Person.select(Person.gender).where(Person.gender == "male")
        db.close()
        return query


class SelectFemale(Select):
    def selectFemale(self):
        query = Person.select(Person.gender).where(Person.gender == "female")
        db.close()
        return query


print(len(SelectMale().selectMale()))
print(len(SelectFemale().selectFemale()))
