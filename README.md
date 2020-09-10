TASK: 
Wczytanie danych z pliku API do bazy danych. Przed zapisem do bazy danych:


stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby
oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)
usuń pole ‘picture’.
W celach szkoleniowych hasło w postaci plaintext też powinno zostać zapisane w bazie.


Na podstawie danych zapisanych w bazie wyświetl:


procent kobiet i mężczyzn
średnią wieku:

ogólną
kobiet
mężczyzn



N najbardziej popularnych miast w formacie: miasto, liczba wystąpień, gdzie N to liczba - parametr przekazywany do programu przez użytkownika, czyli np. dla N = 5 powinno wyświetlić się 5 miast

N najpopularniejszych haseł w formacie: hasło, liczba wystąpień (N, analogicznie jak wyżej)
wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr (format daty jest dowolny, może być np. YYYY-MM-DD)
najbezpieczniejsze hasło - takie, które uzyska najwięcej punktów, gdzie:

jeśli zawiera przynajmniej jedną małą literę otrzymuje 1 punkt
jeśli zawiera przynajmniej jedną dużą literę otrzymuje 2 punkty
jeśli zawiera przynajmniej jedną cyfrę otrzymuje 1 punkt
jeśli zawiera co najmniej 8 znaków - 5 punktów
jeśli zawiera znak specjalny - 3 punkty



Czyli np. hasło “supertajne” uzyska 6 punktów (przynajmniej jedna mała litera i przynajmniej 8 znaków), “Ab1337” uzyska 4 punkty, itd.
Zaprojektowanie interfejsu linii poleceń to część tego zadania. Każdy z tych punktów powinien być zrealizowany jako osobna komenda wywoływana z tego samego skryptu, np.:
python script.py -average-age male
powinno zwrócić średni wiek mężczyzn z bazy danych,
python script.py -most-common-passwords 5
powinno zwrócić pięć najczęstszych haseł użytkowników z bazy.




Before usage Install requiments.txt ( python -m pip install -r requirements.txt )

Commands avalible :

UI.py -h or UI.py --help                                                        Show help message and exit.

UI.py -ct or UI.py --create_table                                               Create empty table person.

UI.py -ft or UI.py --fill_table                                                 Fill table with persons requested from API.

UI.py -gp or UI.py --gender_percentage                                          Returns the percentage of men and women.

UI.py -aa or UI.py --average_age                                                Returns the average age.

UI.py -aam  or UI.py --average_age_male                                         Returns the average age of males.

UI.py -aaf or UI.py --average_age_female                                        Returns the average age of females.

UI.py -bp or UI.py --best_password                                              Returns the best password with points.

UI.py -mcc int or UI.py --most_common_cities int                                Returns the most common city list. Usage example: UI.py -mcc 2

UI.py -mcp int or UI.py --most_common_password int                              Returns the most common password list. Usage example: UI.py -mcp 2

UI.py -bb date_from date_till or UI.py --birthday_between date_from date_till   Returns the most common password list. Date format is yyyy-mm-dd. 
                                                                                Usage example: UI.py -bb 1990-01-12 1991-01-01
                                                                                
You can combine commands in line. For example : UI.py -gp -aa
