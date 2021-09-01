from datetime import datetime


def calculate_age(birthday):
    try:

        now = datetime.now()
        age = (now.year - birthday.year) + \
              (now.month - birthday.month) / 12 + \
              (now.day - birthday.day) / 365

        age = int(age)

        if 5 <= age <= 20:
            age_unit = 'лет'
        elif age % 10 == 1:
            age_unit = 'год'
        elif age % 10 in [2, 3, 4]:
            age_unit = 'года'
        else:
            age_unit = 'лет'

        return f'{age} {age_unit}'
    except (ValueError, IndexError):
        return 'birthday is not valid'
