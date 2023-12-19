# from .models import UserProfile
# from django.contrib import admin
#
# admin.site.register(UserProfile)

from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'gender', 'birthday', 'phone')

    def owner_name(self, obj):
        return obj.owner.username  # Accessing username of the related User instance
    owner_name.short_description = 'Owner Name'


admin.site.register(UserProfile, UserProfileAdmin)
