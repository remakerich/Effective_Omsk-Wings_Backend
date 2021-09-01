from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    url = models.CharField(max_length=100, blank=True, verbose_name='URL')
    logo = models.FileField(null=True, blank=True)
    type = models.CharField(max_length=20,
                            choices=(('general', 'Генеральный партнер'),
                                     ('regular', 'Партнер'),
                                     ('MHL2019', 'Партнер чемпионата МХЛ 2019/2020'),
                                     ('social-media', 'Социальная сеть'),))

    class Meta:
        verbose_name = 'Sponsor or Social Media'
        verbose_name_plural = 'Sponsors & Social Media'

    def __str__(self):
        return self.name
