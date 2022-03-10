from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserModel(User):
    pass

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UserDefinedCode(models.Model):
    name = models.CharField(max_length=8)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Code(models.Model):
    user_defined_code = models.ForeignKey(UserDefinedCode, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=15)

class Document(models.Model):
    title = models.CharField(blank=True, null=True, max_length=200)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)