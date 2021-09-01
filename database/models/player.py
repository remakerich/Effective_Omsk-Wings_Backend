from django.db import models
from database.utils.calculate_age import calculate_age
from database.utils.birthday_long import birthday_long
from database.utils.birthday_short import birthday_short


class Player(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100,
                                choices=(('Вратарь', 'Вратарь'),
                                         ('Защитник', 'Защитник'),
                                         ('Нападающий', 'Нападающий'),)
                                )
    birthday = models.DateField()
    number = models.IntegerField()
    photo = models.ImageField(null=True, blank=True)

    def age(self):
        return calculate_age(self.birthday)

    def birthday_short(self):
        return birthday_short(self.birthday)

    def birthday_long(self):
        return birthday_long(self.birthday)

    def full_name(self):
        return f'{str(self.last_name).strip()} ' \
               f'{str(self.first_name).strip()}'

    def __str__(self):
        return self.full_name()
