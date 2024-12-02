from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model for user-created posts.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Orders posts by latest created


class Review(models.Model):
    """
    Model for reviews on posts.
    """
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE,)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on '{self.post.title}'"

    class Meta:
        ordering = ['-created_at'] 
        unique_together = ('post', 'user')
