def birthday_long(birthday):
    try:

        months = ['января',
                  'февраля',
                  'марта',
                  'апреля',
                  'мая',
                  'июня',
                  'июля',
                  'августа',
                  'сентября',
                  'октября',
                  'ноября',
                  'декабря']

        return f'{birthday.day} {months[birthday.month - 1]} {birthday.year} г.'
    except (ValueError, IndexError):
        return 'birthday is not valid'
