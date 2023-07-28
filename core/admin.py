from django.contrib import admin

from core.models import UserInfo


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'second_name')
    readonly_fields = ['User_photo']
    list_display = ('first_name', 'second_name', 'dob')
    exclude = ['upload', "User_photo"]


admin.site.register(UserInfo, UserInfoAdmin)
