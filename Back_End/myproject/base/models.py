from django.db import models

class User(models.Model):
    username = models.TextField(unique=True, null=False)
    password = models.TextField(null=False)
    is_manager = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'  

    def __str__(self):
        return self.username

class Court(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reserved = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sport = models.TextField(null=False)
    num = models.IntegerField(null=False)

    class Meta:
        db_table = 'courts'  

    def __str__(self):
        return f"{self.sport} Court {self.num}"