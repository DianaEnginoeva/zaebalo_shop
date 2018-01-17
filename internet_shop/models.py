from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    picture = models.TextField()
    describe = models.TextField()
    number_available = models.TextField()
    price = models.TextField()
    number_in_cart = models.TextField()
    cost = models.BooleanField()
    
    def add_to_cart(self):
        self.save()
        
    def __str__(self):
        return self.name