from OrmModel import Person, db
from Request import Request
from PersonPrepare import personDataSelector


class ORM:

    def createTable(self):
        db.create_tables([Person])

    def fillTable(self):
        basePersonsFromAPI = Request().from_api()
        for person in basePersonsFromAPI:
            PersonPrepared = personDataSelector(person)
            Person(daysTillBirthday=PersonPrepared.get("days_till_birthday"),
               gender=PersonPrepared.get("gender"),
               first_name=PersonPrepared.get("first_name"),
               last_name=PersonPrepared.get("last_name"),
               dob=PersonPrepared.get("dob"),
               phone=PersonPrepared.get("phone"),
               cell=PersonPrepared.get("cell"),
               password=PersonPrepared.get("password"),
               city=PersonPrepared.get("city")).save()


ORM().fillTable()
