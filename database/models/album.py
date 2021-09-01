from django.db import models
from django.utils import timezone


class MediaAlbum(models.Model):
    name = models.CharField(max_length=100)
    page_reference = models.CharField(max_length=20,
                                      choices=(('fanclub', 'Фан-клуб'),))
    event_date = models.DateField()
    date_created = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Media Album'
        verbose_name_plural = 'Media Albums'


class MediaFile(models.Model):
    file_url = models.FileField()
    media_album = models.ForeignKey(MediaAlbum,
                                    related_name='media_files',
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.file_url.name
