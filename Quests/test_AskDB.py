from Quests.ask_DB import ManFemalePercentage, AverageAge, BestPassword


def test_calculate_ManFemalePercentage():
    man_female_percentage = ManFemalePercentage()
    list_fifty = []
    list_forty = []
    for x in range(50):
        list_fifty.append(x)
    for x in range(40):
        list_forty.append(x)

    assert man_female_percentage.calculate(["Arek", "Marek", "Czarek"], ["Ala", "Ania", "Wanda"]) == {
        "Percentage_of_male": 50, "Percentage_of_female": 50}

    assert man_female_percentage.calculate(list_fifty, list_forty) == {
        "Percentage_of_male": 55.56, "Percentage_of_female": 44.44}


def test_calculate_AverageAge():
    average_age = AverageAge()

    assert average_age.calculate([10, 10, 10]) == 10
    assert average_age.calculate([55, 60, 23]) == 46
    assert average_age.calculate([55, 60, 24]) == 46.33
    assert average_age.calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5


def test_calculate_BestPassword():
    best_password = BestPassword()
    assert best_password.calculate(["supertajne", "1Qq!11111", "A", "a", "1", "!"]) == {"best_password": "1Qq!11111",
                                                                                        "Password_points": 12}


def test_password_score_BestPassword():
    best_password = BestPassword()
    assert best_password.password_score("supertajne") == {"Password": "supertajne", "Password_points": 6}
    assert best_password.password_score("1Qq!11111") == {"Password": "1Qq!11111", "Password_points": 12}
    assert best_password.password_score("A") == {"Password": "A", "Password_points": 2}
    assert best_password.password_score("a") == {"Password": "a", "Password_points": 1}
    assert best_password.password_score("1") == {"Password": "1", "Password_points": 1}
    assert best_password.password_score("!") == {"Password": "!", "Password_points": 3}


