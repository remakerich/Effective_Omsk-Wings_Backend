from django.db import models


class Season(models.Model):
    season = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    result = models.CharField(max_length=100)
    image = models.FileField()

    def __str__(self):
        return self.season


class Trophy(models.Model):
    event = models.CharField(max_length=100)
    place = models.IntegerField(choices=((1, '1 место'),
                                         (2, '2 место'),
                                         (3, '3 место'),))
    season = models.ForeignKey(Season,
                               related_name='trophies',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.event

    class Meta:
        verbose_name = 'Trophy'
        verbose_name_plural = 'Trophies'
