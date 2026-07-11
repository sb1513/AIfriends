from django.contrib import admin
from web.models.user import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)  #逗号不要删,加了逗号表示传入一个元组