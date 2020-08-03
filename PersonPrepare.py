from datetime import datetime
import re


def tillBirthdayCalc(personFromAPI):
    currentDate = datetime.now()
    person_birthday = datetime.strptime(personFromAPI.get('dob').get('date'), "%Y-%m-%dT%H:%M:%S.%fZ")

    try:
        if datetime(currentDate.year, person_birthday.month, person_birthday.day) >= datetime(currentDate.year,
                                                                                              currentDate.month,
                                                                                              currentDate.day):
            delta = datetime(currentDate.year, person_birthday.month, person_birthday.day)
        else:

            delta = datetime(currentDate.year + 1, person_birthday.month, person_birthday.day)
    # When person is born 29.02, we catch it and calculate days till birthday to the closest leap year.
    # In that way you can sometimes see in database that someone have higher value than 365 days till birthday.
    except ValueError:
        leapYear = True
        i = 1
        while leapYear:
            i += 1
            try:
                delta = datetime(currentDate.year + i, person_birthday.month, person_birthday.day)
                leapYear = False
            except ValueError:
                leapYear = True

    daysTillBirthday = (currentDate - delta).days
    return abs(daysTillBirthday)


def personDataSelector(personFromAPI):
    daysTillBirthday = tillBirthdayCalc(personFromAPI)
    PersonMatchingDb = {
        "uuid": personFromAPI.get('login').get('uuid'),
        "days_till_birthday": daysTillBirthday,
        "age" : personFromAPI.get('dob').get('age'),
        "gender": personFromAPI.get('gender'),
        "first_name": personFromAPI.get('name').get('first'),
        "last_name": personFromAPI.get('name').get('last'),
        "dob": personFromAPI.get('dob').get('date'),
        "phone": re.sub("[^0-9]", "", personFromAPI.get('phone')),
        "cell": re.sub("[^0-9]", "", personFromAPI.get('cell')),
        "password": personFromAPI.get('login').get('password'),
        "city": personFromAPI.get('location').get('city')
    }

    return PersonMatchingDb
