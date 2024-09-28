from django.db import models


class BookModel(models.Model):
    image = models.ImageField(upload_to='books/images/')
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey('categories.CategoryModel', related_name='books', on_delete=models.SET_NULL,
                                 null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'
