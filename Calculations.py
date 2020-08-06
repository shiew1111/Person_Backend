from ORM import *


class Calculations:
    def manFemalePercentage(self):
        maleRepresentation = len(SelectMale().selectMale())
        femaleRepresentation = len(SelectFemale().selectFemale())
        percentageMale = (maleRepresentation / (maleRepresentation + femaleRepresentation)) * 100
        percentageFemale = 100 - percentageMale
        return {"Percentage_of_male": percentageMale, "Percentage_of_female": percentageFemale}

    class AvarageAge:
        def avarageAgeCalculate(self):
            sum = 0
            personsAge = SelectAge.selectAge(self)
            for age in personsAge:
                sum += age.age

            avarageAge = sum / len(personsAge)

            return avarageAge

    class AvarageAgeMale(AvarageAge):
        def avarageMaleAgeCalculate(self):
            sum = 0
            personsAge = SelectMaleAge.selectMaleAge(self)
            for age in personsAge:
                sum += age.age

            avarageAge = sum / len(personsAge)

            return avarageAge

    class AvarageAgeFemale(AvarageAge):
        def avarageFemaleAgeCalculate(self):
            sum = 0
            personsAge = SelectFemaleAge.selectFemaleAge(self)
            for age in personsAge:
                print(age.age)
                sum += age.age

            avarageAge = sum / len(personsAge)

            return avarageAge

    class MostPopularCity:
        def mostPopularCityList(self, limit=5):
            popularCities = SelectMostPopularCity().selectMostPopular(limit=limit)
            popularCitiesList = []
            for city in popularCities:
                popularCitiesList.append({"City": city.city, "Count": city.count})

            return popularCitiesList

    class MostPopularPassword:
        def mostPopularPasswordList(self, limit=5):
            popularPassword = SelectMostPopularPassword().selectMostPopular(limit=limit)
            popularPasswordList = []
            for city in popularPassword:
                popularPasswordList.append({"Password": city.password, "Count": city.count})

            return popularPasswordList

    class BestPassword:
        def BestPasswordCalc(self):

            passwords = LongPassword().selectLongPassword()
            passwordsDictList = []
            for password in passwords:

                passwordDict = {"Password": password.password, "Password_points": 5}

                if any(c for c in password.password if not c.isalnum()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 3
                if any(c for c in password.password if c.isnumeric()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 1
                if any(c for c in password.password if c.islower()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 1
                if any(c for c in password.password if c.isupper()):
                    passwordDict["Password_points"] = passwordDict["Password_points"] + 2
                passwordsDictList.append(passwordDict)

            bestPasswordPoints = max([x['Password_points'] for x in passwordsDictList])

            for x in passwordsDictList:
                if x['Password_points'] == bestPasswordPoints:
                    bestPassword = x["Password"]
                    return {"bestPassword": bestPassword, "PasswordPoints": bestPasswordPoints}


print(Calculations().BestPassword().BestPasswordCalc())
