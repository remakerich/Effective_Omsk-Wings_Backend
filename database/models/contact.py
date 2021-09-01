from django.db import models


class Contact(models.Model):
    contact = models.CharField(max_length=100)
    line1 = models.CharField(max_length=100,
                             verbose_name='Fist Line')
    line2 = models.CharField(max_length=100,
                             verbose_name='Second Line',
                             blank=True)
    line3 = models.CharField(max_length=100,
                             verbose_name='Third Line',
                             blank=True)

    def __str__(self):
        return self.contact
