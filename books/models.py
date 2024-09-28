from django.db import models


class BookModel(models.Model):
    image = models.ImageField(upload_to='books/images/')
