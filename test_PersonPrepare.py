from datetime import datetime, timedelta
import mock

import PersonPrepare
from PersonPrepare import till_birthday_calc, person_data_selector


def test_till_birthday_calc():
    today_minus_two_days = datetime.now() + timedelta(days=2)
    today_minus_two_days = today_minus_two_days.strftime("%Y-%m-%d") + "T" + today_minus_two_days.strftime(
        "%H:%M:%S.%fZ")
    today_plus_two_days = datetime.now() - timedelta(days=2)
    today_plus_two_days = today_plus_two_days.strftime("%Y-%m-%d") + "T" + today_plus_two_days.strftime(
        "%H:%M:%S.%fZ")
    assert till_birthday_calc({"gender": "female", "name": {"title": "Miss", "first": "Louane", "last": "Vidal"},
                               "location": {"street": {"number": 2479, "name": "Place du 8 Février 1962"},
                                            "city": "Avignon",
                                            "state": "Vendée", "country": "France", "postcode": 78276,
                                            "coordinates": {"latitude": "2.0565", "longitude": "95.2422"},
                                            "timezone": {"offset": "+1:00",
                                                         "description": "Brussels, Copenhagen, Madrid, Paris"}},
                               "email": "louane.vidal@example.com",
                               "login": {"uuid": "9f07341f-c7e6-45b7-bab0-af6de5a4582d", "username": "angryostrich988",
                                         "password": "r2d2", "salt": "B5ywSDUM",
                                         "md5": "afce5fbe8f32bcec1a918f75617ab654",
                                         "sha1": "1a5b1afa1d9913cf491af64ce78946d18fea6b04",
                                         "sha256": "0124895aa1e6e5fb0596fad4c413602e0922e8a8c2dc758bbdb3fa070ad25a07"},
                               "dob": {"date": str(today_minus_two_days), "age": 54},
                               "registered": {"date": "2016-08-11T06:51:52.086Z", "age": 4}, "phone": "02-62-35-18-98",
                               "cell": "06-07-80-83-11", "id": {"name": "INSEE", "value": "2NNaN01776236 16"},
                               "picture": {"large": "https://randomuser.me/api/portraits/women/88.jpg",
                                           "medium": "https://randomuser.me/api/portraits/med/women/88.jpg",
                                           "thumbnail": "https://randomuser.me/api/portraits/thumb/women/88.jpg"},
                               "nat": "FR"}) == 2
    assert till_birthday_calc({"gender": "female", "name": {"title": "Miss", "first": "Louane", "last": "Vidal"},
                               "location": {"street": {"number": 2479, "name": "Place du 8 Février 1962"},
                                            "city": "Avignon",
                                            "state": "Vendée", "country": "France", "postcode": 78276,
                                            "coordinates": {"latitude": "2.0565", "longitude": "95.2422"},
                                            "timezone": {"offset": "+1:00",
                                                         "description": "Brussels, Copenhagen, Madrid, Paris"}},
                               "email": "louane.vidal@example.com",
                               "login": {"uuid": "9f07341f-c7e6-45b7-bab0-af6de5a4582d", "username": "angryostrich988",
                                         "password": "r2d2", "salt": "B5ywSDUM",
                                         "md5": "afce5fbe8f32bcec1a918f75617ab654",
                                         "sha1": "1a5b1afa1d9913cf491af64ce78946d18fea6b04",
                                         "sha256": "0124895aa1e6e5fb0596fad4c413602e0922e8a8c2dc758bbdb3fa070ad25a07"},
                               "dob": {"date": str(today_plus_two_days), "age": 54},
                               "registered": {"date": "2016-08-11T06:51:52.086Z", "age": 4}, "phone": "02-62-35-18-98",
                               "cell": "06-07-80-83-11", "id": {"name": "INSEE", "value": "2NNaN01776236 16"},
                               "picture": {"large": "https://randomuser.me/api/portraits/women/88.jpg",
                                           "medium": "https://randomuser.me/api/portraits/med/women/88.jpg",
                                           "thumbnail": "https://randomuser.me/api/portraits/thumb/women/88.jpg"},
                               "nat": "FR"}) == 363


# def i'll used to mocking till_birthday_calc in test_person_data_selector.
def mock_till_birthday_calc(arg):
    return 2


def test_person_data_selector():
    with mock.patch.object(PersonPrepare, 'till_birthday_calc', new=mock_till_birthday_calc):
        assert person_data_selector(
            {"gender": "female", "name": {"title": "Miss", "first": "Louane", "last": "Vidal"},
             "location": {"street": {"number": 2479, "name": "Place du 8 Février 1962"}, "city": "Avignon",
                          "state": "Vendée", "country": "France", "postcode": 78276,
                          "coordinates": {"latitude": "2.0565", "longitude": "95.2422"},
                          "timezone": {"offset": "+1:00",
                                       "description": "Brussels, Copenhagen, Madrid, Paris"}},
             "email": "louane.vidal@example.com",
             "login": {"uuid": "9f07341f-c7e6-45b7-bab0-af6de5a4582d", "username": "angryostrich988",
                       "password": "r2d2", "salt": "B5ywSDUM", "md5": "afce5fbe8f32bcec1a918f75617ab654",
                       "sha1": "1a5b1afa1d9913cf491af64ce78946d18fea6b04",
                       "sha256": "0124895aa1e6e5fb0596fad4c413602e0922e8a8c2dc758bbdb3fa070ad25a07"},
             "dob": {"date": "1966-06-26T11:50:25.558Z", "age": 54},
             "registered": {"date": "2016-08-11T06:51:52.086Z", "age": 4}, "phone": "02-62-35-18-98",
             "cell": "06-07-80-83-11", "id": {"name": "INSEE", "value": "2NNaN01776236 16"},
             "picture": {"large": "https://randomuser.me/api/portraits/women/88.jpg",
                         "medium": "https://randomuser.me/api/portraits/med/women/88.jpg",
                         "thumbnail": "https://randomuser.me/api/portraits/thumb/women/88.jpg"},
             "nat": "FR"}) == {
                   "uuid": "9f07341f-c7e6-45b7-bab0-af6de5a4582d",
                   "days_till_birthday": 2,
                   "age": 54,
                   "gender": "female",
                   "first_name": "Louane",
                   "last_name": "Vidal",
                   "dob": "1966-06-26T11:50:25.558Z",
                   "phone": "0262351898",
                   "cell": "0607808311",
                   "password": "r2d2",
                   "city": "Avignon"
               }
