import argparse
import datetime

from ask_DB import ManFemalePercentage, AverageAge, AverageAgeMale, AverageAgeFemale, BestPassword, MostCommonCity, \
    MostCommonPassword, BirthdayBetween
from ObjectRelationalMapping.orm import ORM


def console_interface():
    parser = argparse.ArgumentParser(description='Parse orders and arguments')

    parser.add_argument('-ct', '--create_table', dest='create_table', action="store_true",
                        help='Create empty table person')

    parser.add_argument('-ft', '--fill_table', dest='fill_table', action="store_true",
                        help='Fill table with persons requested from API')

    parser.add_argument('-gp', '--gender_percentage', dest='gender_percentage', action="store_true",
                        help='Returns the percentage of men and women')
    parser.add_argument('-aa', '--average_age', dest='average_age', action="store_true", help='Returns the average age')
    parser.add_argument('-aam', '--average_age_male', dest='average_age_male', action="store_true",
                        help='Returns the average age of males')
    parser.add_argument('-aaf''--average_age_female', dest='average_age_female', action="store_true",
                        help='Returns the average age of females')
    parser.add_argument('-bp', '--best_password', dest='best_password', action="store_true",
                        help='Returns the best password with points.')

    parser.add_argument('-mcc', '--most_common_cities', metavar='int', dest='most_common_city', nargs='?', const=5,
                        type=int,
                        help='Returns the most common city list. Usage example: UI.py -mcc 2')
    parser.add_argument('-mcp', '--most_common_password', metavar='int', dest='most_common_password', nargs='?',
                        const=5, type=int,
                        help='Returns the most common password list. Usage example: UI.py -mcp 2')

    parser.add_argument('-bb', '--birthday_between', metavar=('date_from', 'date_till'), dest='birthday_between',
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), nargs=2,
                        help='Returns the most common password list. Date format is yyyy-mm-dd. Usage example: UI.py -bb '
                             '1990-01-12 1991-01-01')

    args = parser.parse_args()

    fill_table = args.fill_table
    create_table = args.create_table
    gender_percentage = args.gender_percentage
    average_age = args.average_age
    average_age_male = args.average_age_male
    average_age_female = args.average_age_female
    best_password = args.best_password
    most_common_city = args.most_common_city
    most_common_password = args.most_common_password
    birthday_between = args.birthday_between

    if create_table:
        ORM().create_table()
    if fill_table:
        ORM().fill_table()
    if gender_percentage:
        print(ManFemalePercentage().get())
    if average_age:
        print(AverageAge().get())
    if average_age_male:
        print(AverageAgeMale().get())
    if average_age_female:
        print(AverageAgeFemale().get())
    if best_password:
        print(BestPassword().get())
    if most_common_city:
        print(MostCommonCity(limit=most_common_city).get())
    if most_common_password:
        print(MostCommonPassword(limit=most_common_password).get())
    if birthday_between:
        yearFrom = birthday_between[0].year
        monthFrom = birthday_between[0].month
        dayFrom = birthday_between[0].day
        yearTill = birthday_between[1].year
        monthTill = birthday_between[1].month
        dayTill = birthday_between[1].day

        print(BirthdayBetween(year_from=yearFrom, month_from=monthFrom, day_from=dayFrom, year_till=yearTill,
                                      month_till=monthTill, day_till=dayTill).get())


if __name__ == "__main__":
    console_interface()
