from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character
from web.models.friend import Friend, Message,SystemPrompt

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)  #逗号不要删,加了逗号表示传入一个元组


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    raw_id_fields = ('me','character',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    raw_id_fields = ('friend',)


admin.site.register(SystemPrompt)