from django.contrib import admin
from blog.models import Post, Contact, Tag, ZipCode


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(Tag)


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'gu', 'dong', 'road']

admin.site.register(ZipCode, ZipCodeAdmin)
