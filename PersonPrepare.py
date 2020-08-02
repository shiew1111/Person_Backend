from datetime import datetime
import re


def tillBirthdayCalc(personFromAPI):
    currentDate = datetime.now()
    person_birthday = datetime.strptime(personFromAPI.get('dob').get('date'), "%Y-%m-%dT%H:%M:%S.%fZ")
    if datetime(currentDate.year, person_birthday.month, person_birthday.day) >= datetime(currentDate.year,
                                                                                          currentDate.month,
                                                                                          currentDate.day):
        delta = datetime(currentDate.year, person_birthday.month, person_birthday.day)
    else:
        # catch error i wstaw coś gdyby był rok przystępony i 29 jebany lutego
        delta = datetime(currentDate.year + 1, person_birthday.month, person_birthday.day)
    daysTillBirthday = (delta - currentDate).days + 1
    return abs(daysTillBirthday)


def personDataSelector(personFromAPI):
    daysTillBirthday = tillBirthdayCalc(personFromAPI)
    PersonMatchingDb = {
        "days_till_birthday": daysTillBirthday,
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
