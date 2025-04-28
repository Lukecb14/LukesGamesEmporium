from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

    def __str__(self):
        return self.user.username

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    score = models.IntegerField(null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rawData = models.TextField()

    def __str__(self):
        return (str(self.user) + ": " + str(self.score) + " on " + str(self.game) + " (" + str(self.date) + ")")
    
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requestFrom', null=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requestTo",null=False)

    def __str__(self):
        return("Freind request from " + str(self.userFrom) + " to " + str(self.userTo))

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends', null=False)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendOf', null=False)

    def __str__(self):
        return (str(self.user) + " is friends with " + str(self.friend))