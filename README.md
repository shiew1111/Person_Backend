



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
