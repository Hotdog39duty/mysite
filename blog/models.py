from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model for user-created posts.

    Attributes
    ----------
    title : CharField
        The title of the post.
    content : TextField
        The content of the post.
    author : ForeignKey
        The user who created the post.
    created_at : DateTimeField
        The date and time when the post was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the Post model.

        Returns
        -------
        str
            The title of the post.
        """
        return self.title

    class Meta:
        """
        Meta options for the Post model.

        Attributes
        ----------
        ordering : list
            Orders posts by latest created.
        """
        ordering = ['-created_at']


class Review(models.Model):
    """
    Model for reviews on posts.

    Attributes
    ----------
    post : ForeignKey
        The post being reviewed.
    user : ForeignKey
        The user who wrote the review.
    content : TextField
        The content of the review.
    rating : IntegerField
        The rating given by the user.
    created_at : DateTimeField
        The date and time when the review was created.
    """
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the Review model.

        Returns
        -------
        str
            A string indicating the user and the post reviewed.
        """
        return f"Review by {self.user.username} on '{self.post.title}'"

    class Meta:
        """
        Meta options for the Review model.

        Attributes
        ----------
        ordering : list
            Orders reviews by latest created.
        unique_together : tuple
            Ensures a user can only review a post once.
        """
        ordering = ['-created_at']
        unique_together = ('post', 'user')
