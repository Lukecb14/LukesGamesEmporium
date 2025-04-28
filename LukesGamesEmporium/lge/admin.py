from django.contrib import admin
from lge.models import UserProfile, Game, Score, FriendRequest, Friends
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

admin.site.register(Game)
admin.site.register(Score)
admin.site.register(UserProfile)
admin.site.register(FriendRequest)
admin.site.register(Friends)