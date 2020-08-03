from peewee import chunked

from OrmModel import Person, db
from Request import Request
from PersonPrepare import personDataSelector


class ORM:

    def createTable(self):
        db.create_tables([Person])

    def fillTable(self):

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
            for batch in chunked(PersonPreparedList, 100):
                # Executing 100 rows from list.
                Person.insert_many(batch).execute()

        print("Records saved! Closing database connection!")
        db.close()


ORM().fillTable()
