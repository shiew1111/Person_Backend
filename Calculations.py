from ORM import SelectFemale, SelectMale


class Calculations:
    def manFemalePercentage(self):
        maleRepresentation = len(SelectMale().selectMale())
        femaleRepresentation = len(SelectFemale().selectFemale())
        percentageMale = (maleRepresentation / (maleRepresentation + femaleRepresentation)) * 100
        percentageFemale = 100 - percentageMale
        return {"Percentage_of_male": percentageMale, "Percentage_of_female": percentageFemale}


print(Calculations().manFemalePercentage())
