from django.contrib import admin
from .models import AboutPage, GlobalChatMessage, Post, PostChatMessage

admin.site.register(AboutPage)
admin.site.register(Post)
admin.site.register(GlobalChatMessage)
admin.site.register(PostChatMessage)