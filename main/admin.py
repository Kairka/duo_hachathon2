from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]

admin.site.register(Region)
