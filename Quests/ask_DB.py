from ObjectRelationalMapping.orm import SelectFemale, SelectMale, SelectAge, SelectMaleAge, SelectFemaleAge, \
    SelectMostPopularCity, SelectMostPopularPassword, SelectPassword, SelectBirthdayBetween


class _Select:
    def select_from_db(self, select):
        return select.select()


class ManFemalePercentage(_Select):
    def get(self):
        male_representation = self.select_from_db(SelectMale())
        female_representation = self.select_from_db(SelectFemale())
        return self.calculate(male_representation, female_representation)

    def calculate(self, males_lisy, females_list):
        male_representation_length = len(males_lisy)
        female_representation_length = len(females_list)
        percentage_male = (male_representation_length / (
                male_representation_length + female_representation_length)) * 100
        percentage_female = 100 - percentage_male
        return {"Percentage_of_male": round(percentage_male, 2),
                "Percentage_of_female": round(percentage_female, 2)}


class AverageAge(_Select):
    def get(self):
        persons_age = self.select_from_db(SelectAge())
        return self.calculate(persons_age)

    def calculate(self, persons_age):
        sum = 0
        for age in persons_age:
            sum += age

        averageAge = sum / len(persons_age)

        return round(averageAge, 2)


class AverageAgeMale(AverageAge):
    def get(self):
        persons_age = self.select_from_db(SelectMaleAge())
        return self.calculate(persons_age)


class AverageAgeFemale(AverageAge):
    def get(self):
        persons_age = self.select_from_db(SelectFemaleAge())
        return self.calculate(persons_age)


class MostCommonCity(_Select):
    def __init__(self, limit=5):
        self.limit = limit

    def get(self):
        popular_cities = self.select_from_db(SelectMostPopularCity(self.limit))

        return popular_cities


class MostCommonPassword(_Select):
    def __init__(self, limit=5):
        self.limit = limit

    def get(self, ):
        popular_password = self.select_from_db(SelectMostPopularPassword(self.limit))

        return popular_password


class BestPassword(_Select):
    def get(self):

        passwords = self.select_from_db(SelectPassword())
        return self.calculate(passwords)

    def calculate(self, passwordsList):

        passwords_dict_list = []
        for password in passwordsList:
            passwords_dict_list.append(self.password_score(password))

        best_password_points = max([x['Password_points'] for x in passwords_dict_list])

        for x in passwords_dict_list:
            if x['Password_points'] == best_password_points:
                best_password = x["Password"]
                return {"best_password": best_password, "Password_points": best_password_points}

    def password_score(self, password):

        password_dict = {"Password": password, "Password_points": 0}
        if len(password) >= 8:
            password_dict["Password_points"] += 5
        if any(c for c in password if not c.isalnum()):
            password_dict["Password_points"] += 3
        if any(c for c in password if c.isnumeric()):
            password_dict["Password_points"] += 1
        if any(c for c in password if c.islower()):
            password_dict["Password_points"] += 1
        if any(c for c in password if c.isupper()):
            password_dict["Password_points"] += 2
        return password_dict


class BirthdayBetween(_Select):
    def __init__(self, year_from, month_from, day_from, year_till, month_till, day_till):
        self.day_till = day_till
        self.month_till = month_till
        self.year_till = year_till
        self.day_from = day_from
        self.month_from = month_from
        self.year_from = year_from

    def get(self):
        return self.select_from_db(
            SelectBirthdayBetween(self.year_from, self.month_from, self.day_from, self.year_till, self.month_till,
                                  self.day_till))
