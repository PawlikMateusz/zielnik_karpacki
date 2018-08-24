from django.contrib import admin
from django.shortcuts import get_object_or_404
from . import models
from multiupload.admin import MultiUploadAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class ImagesInlineAdmin(admin.TabularInline):
    model = models.Images


class RoslinaMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, nazwa_polska, request):
        if nazwa_polska:
            image = nazwa_polska.images.create(file=uploaded)
        else:
            image = Images.objects.create(file=uploaded, nazwa_polska=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }

class RoslinaAdmin(RoslinaMultiuploadMixing, MultiUploadAdmin):
    search_fields = ["nazwa_polska"]
    list_filter = ["nazwa_polska"]
    inlines = [ImagesInlineAdmin,]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Images, pk=pk)
        return obj.delete()


class ImagesAdmin(RoslinaMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True


admin.site.register(models.Roslina, RoslinaAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
