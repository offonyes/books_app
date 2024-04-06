from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.name
