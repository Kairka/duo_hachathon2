from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tour', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Region)
