from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        elif self.user.first_name:
            return self.user.first_name
        elif self.user.last_name:
            return self.user.last_name
        else:
            return self.user.username

class Author(models.Model):
    full_name = models.CharField(max_length=255)
    spesialist = models.CharField(max_length=255)
    bio = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reaction(models.Model):
    artecle = models.ForeignKey(Article, related_name='reactions', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='reacts', on_delete=models.SET_NULL, null=True, blank=True)
    reaction = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.person}'s react for {self.artecle}"

class Comment(models.Model):
    artecle = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='comments', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.person}'s comment for {self.artecle}: {self.comment}"