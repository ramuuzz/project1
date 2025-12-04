from django.db import models

# Create your models here.
class mens(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='mens/')

    def __str__(self):
        return self.name

class womens(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='womens/')

    def __str__(self):
        return self.name
class accessoriess(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='accessories/')

    def __str__(self):
        return self.name
class cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item_id = models.IntegerField()
    item_type = models.CharField(max_length=20)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item_name} for {self.user.username}"