from AskDB import AskDB


def test_calculate_ManFemalePercentage():
    ManFemalePercentage = AskDB().ManFemalePercentage()
    assert ManFemalePercentage.calculate(["Arek", "Marek", "Czarek"], ["Ala", "Ania", "Wanda"]) == {"Percentage_of_male": 50, "Percentage_of_female": 50}
