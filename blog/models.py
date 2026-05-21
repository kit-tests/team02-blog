from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class AboutPage(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Page"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class GlobalChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="global_chat_messages")
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]

    def __str__(self):
        return f"Global chat by {self.user.username}"


class PostChatMessage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="chat_messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_chat_messages")
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]

    def __str__(self):
        return f"Post chat on {self.post.slug} by {self.user.username}"
