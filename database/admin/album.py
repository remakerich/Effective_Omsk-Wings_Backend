from django.contrib import admin
from database.models import *
from django.utils.html import mark_safe


def image_preview(obj):
    if len(obj.file_url) == 0:
        return
    return mark_safe('<img src="/media/%s" width="200" />' % obj.file_url)


class MediaFileInline(admin.StackedInline):
    model = MediaFile
    extra = 0
    readonly_fields = [image_preview]


@admin.register(MediaAlbum)
class MediaAlbumAdmin(admin.ModelAdmin):
    inlines = [MediaFileInline]
    list_display = ['name',
                    'page_reference',
                    'event_date',
                    'date_created']
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.save()

        for file in request.FILES.getlist('photos_multiple'):
            obj.media_files.create(file_url=file)
