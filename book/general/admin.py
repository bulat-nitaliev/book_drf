from django.contrib import admin
from general.models import User, Book
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )

    readonly_fields = ("date_joined","last_login",)

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "genre",
        "user",
        "using_the_book",
    )

    # readonly_fields = ("user",)
