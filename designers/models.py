from django.db import models

# Create your models here.
CATEGORY_CHOICES= [
    ('mensfashion', 'Mensfashion'),
    ('womensfashion', 'Womensfashion'),
    ]

class Image(models.Model):
    class Meta:
        ordering = ['price']
    name = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=100, decimal_places=2)

    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="mensfashion")
    image=models.ImageField(upload_to="img/%y")
    price = models.FloatField()
    def str(self):
        return f'{self.name,self.image}'

# class ProductImage(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="mensfashion")
#     image=models.ImageField(upload_to="img/%y")
#     def str(self):
#         return f'{self.name,self.image}'
