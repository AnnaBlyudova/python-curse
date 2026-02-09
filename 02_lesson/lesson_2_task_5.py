
def month_to_season(month):
    if month <= 3:
        return ('Зима')
    elif month > 3 and month <= 6:
        return ('Весна')
    elif month > 6 and month <= 9:
        return ('Лето')
    elif month > 9 and month <= 12:
        return ('Осень')
    else:
        return "Неверный номер месяца"


month = int(input('Введите номер месяца: '))

print(month_to_season(month))
