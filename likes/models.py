from django.db import models
from django.contrib.auth.models import User
from poems.models import Poem


class Like(models.Model):
    """
    Like model, related to User and Poem.
    'owner' is a User instance and 'poem’ is a Poem instance.
    'unique_together' makes sure a user can't like the same poem twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(
        Poem, related_name='likes', on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'poem']

    def __str__(self):
        return f"{self.poem} {self.owner}"
