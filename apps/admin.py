from django.contrib import admin

from apps.models import User, Photo, Post


class ProductImageStackedInline(admin.StackedInline):
    model = Photo
    min_num = 1
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'address', 'phone', 'website', 'company')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)