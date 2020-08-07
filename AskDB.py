from ORM import *


class AskDB:
    class _Select:
        def select_from_db(self, select):
            return select.select()

    class ManFemalePercentage(_Select):
        def get(self):
            maleRepresentation = len(self.select_from_db(SelectMale()))
            femaleRepresentation = len(self.select_from_db(SelectFemale()))
            percentageMale = (maleRepresentation / (maleRepresentation + femaleRepresentation)) * 100
            percentageFemale = 100 - percentageMale
            return {"Percentage_of_male": percentageMale, "Percentage_of_female": percentageFemale}

    class AverageAge(_Select):
        def get(self):
            sum = 0
            personsAge = self.select_from_db(SelectAge())
            for age in personsAge:
                sum += age

            averageAge = sum / len(personsAge)

            return averageAge

    class AverageAgeMale(AverageAge):
        def get(self):
            sum = 0
            personsAge = self.select_from_db(SelectMaleAge())
            for age in personsAge:
                sum += age

            averageAge = sum / len(personsAge)

            return averageAge

    class AverageAgeFemale(AverageAge):
        def get(self):
            sum = 0
            personsAge = self.select_from_db(SelectFemaleAge())
            for age in personsAge:
                sum += age

            avarageAge = sum / len(personsAge)

            return avarageAge

    class MostCommonCity(_Select):
        def __init__(self, limit=5):
            self.limit = limit

        def get(self):
            popularCities = self.select_from_db(SelectMostPopularCity(self.limit))

            return popularCities

    class MostCommonPassword(_Select):
        def __init__(self, limit=5):
            self.limit = limit

        def get(self, ):
            popularPassword = self.select_from_db(SelectMostPopularPassword(self.limit))

            return popularPassword

    class BestPassword(_Select):
        def get(self):

            passwords = self.select_from_db(SelectLongPassword())
            passwordsDictList = []
            for password in passwords:

                passwordDict = {"Password": password, "Password_points": 5}

                if any(c for c in password if not c.isalnum()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 3
                if any(c for c in password if c.isnumeric()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 1
                if any(c for c in password if c.islower()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 1
                if any(c for c in password if c.isupper()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 2
                passwordsDictList.append(passwordDict)

            bestPasswordPoints = max([x['Password_points'] for x in passwordsDictList])

            for x in passwordsDictList:
                if x['Password_points'] == bestPasswordPoints:
                    bestPassword = x["Password"]
                    return {"bestPassword": bestPassword, "PasswordPoints": bestPasswordPoints}

    class BirthdayBetween(_Select):
        def __init__(self, yearFrom, monthFrom, dayFrom, yearTill, monthTill, dayTill):
            self.dayTill = dayTill
            self.monthTill = monthTill
            self.yearTill = yearTill
            self.dayFrom = dayFrom
            self.monthFrom = monthFrom
            self.yearFrom = yearFrom

        def get(self):
            return self.select_from_db(
                SelectBirthdayBetween(self.yearFrom, self.monthFrom, self.dayFrom, self.yearTill, self.monthTill,
                                      self.dayTill))

# print(AskDB().BestPassword().get())
