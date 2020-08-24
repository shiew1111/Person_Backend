from datetime import datetime
import re


def till_birthday_calc(personFromAPI):
    current_date = datetime.now()
    person_birthday = datetime.strptime(personFromAPI.get('dob').get('date'), "%Y-%m-%dT%H:%M:%S.%fZ")

    try:
        if datetime(current_date.year, person_birthday.month, person_birthday.day) >= datetime(current_date.year,
                                                                                               current_date.month,
                                                                                               current_date.day):
            delta = datetime(current_date.year, person_birthday.month, person_birthday.day)
        else:

            delta = datetime(current_date.year + 1, person_birthday.month, person_birthday.day)
    # When person is born 29.02, we catch it and calculate days till birthday to the closest leap year.
    # In that way you can sometimes see in database that someone have higher value than 365 days till birthday.
    except ValueError:
        leap_year = True
        i = 1
        while leap_year:
            i += 1
            try:
                delta = datetime(current_date.year + i, person_birthday.month, person_birthday.day)
                leap_year = False
            except ValueError:
                leap_year = True

    days_till_birthday = (current_date - delta).days
    return abs(days_till_birthday)


def person_data_selector(personFromAPI):
    days_till_birthday = till_birthday_calc(personFromAPI)
    phone = re.sub("[^0-9]", "", personFromAPI.get('phone'))
    cell = re.sub("[^0-9]", "", personFromAPI.get('cell'))
    person_matching_db = {
        "uuid": personFromAPI.get('login').get('uuid'),
        "days_till_birthday": days_till_birthday,
        "age": personFromAPI.get('dob').get('age'),
        "gender": personFromAPI.get('gender'),
        "first_name": personFromAPI.get('name').get('first'),
        "last_name": personFromAPI.get('name').get('last'),
        "dob": personFromAPI.get('dob').get('date'),
        "phone": str(phone),
        "cell": str(cell),
        "password": personFromAPI.get('login').get('password'),
        "city": personFromAPI.get('location').get('city')
    }

    return person_matching_db
