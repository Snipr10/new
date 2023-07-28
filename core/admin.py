from django.contrib import admin

from core.models import UserInfo


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'second_name')
    readonly_fields = ['User_preview']
    list_display = ('first_name', 'second_name', 'dob')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['User_photo']
        return []

    def get_exclude(self, request, obj=None):
        if obj:
            return ['upload']
        return []


admin.site.register(UserInfo, UserInfoAdmin)
