def birthday_short(birthday):
    try:
        return f'{f"{birthday.day:02d}"}.{f"{birthday.month:02d}"}.{birthday.year}'
    except (ValueError, IndexError):
        return 'birthday is not valid'
