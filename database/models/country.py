from django.db import models


class FanClubCountry(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Fan Club Country'
        verbose_name_plural = 'Fan Club Countries'


class City(models.Model):
    city = models.CharField(max_length=100)
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    country = models.ForeignKey(FanClubCountry,
                                related_name='cities',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
