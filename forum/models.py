from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
