from django.db import models
from database.utils.calculate_age import calculate_age
from database.utils.birthday_long import birthday_long
from database.utils.birthday_short import birthday_short
from database.utils.split_about import split_about


class Employee(models.Model):
    order = models.IntegerField(verbose_name='Webpage order (top to bottom)')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=20,
                                  choices=(('Руководство', 'Руководство'),
                                           ('Тренерский штаб', 'Тренерский штаб'),
                                           ('Персонал', 'Персонал'),))
    birthday = models.DateField()
    about = models.TextField(max_length=1000)
    photo = models.ImageField(null=True, blank=True)

    def full_name(self):
        return f'{str(self.last_name).strip()} ' \
               f'{str(self.first_name).strip()} ' \
               f'{str(self.middle_name).strip()}'

    def __str__(self):
        return self.full_name()

    def age(self):
        return calculate_age(self.birthday)

    def birthday_long(self):
        return birthday_long(self.birthday)

    def birthday_short(self):
        return birthday_short(self.birthday)

    def about_short(self):
        return split_about(self.about)[0]

    def about_dropdown(self):
        return split_about(self.about)[1]


class Achievement(models.Model):
    years = models.CharField(max_length=11)
    achievement = models.CharField(max_length=225)
    employee = models.ForeignKey(Employee,
                                 related_name='achievements',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.years
