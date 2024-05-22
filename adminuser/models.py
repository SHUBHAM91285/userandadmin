from django.db import models

# Create your models here.
class AdminModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.username+" "+self.email+" "+self.role


class App(models.Model):
    app = models.CharField(max_length=50)
    points = models.CharField(max_length=50)

    def __str__(self):
        return self.app+" "+self.points
    
class Image(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name="image")
    apps = models.ManyToManyField(App, blank=True, related_name="apps")

    def __str__(self):
        return self.username+" "+self.email+" "+self.role
