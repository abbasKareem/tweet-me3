import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# superuser passowrd: 0000123400, username: abbas, email: blank
class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #  many user can have many tweets
    image = models.FileField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 299)
        }

    