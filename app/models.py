from django.db import models

# Create your models here.
class Product_Category(models.Model):
    pcid=models.PositiveIntegerField(primary_key=True)
    pcname=models.CharField(max_length=100)
    def __str__(self):
        return self.pcname

class Product(models.Model):
    pcname=models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    pid=models.PositiveIntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.DecimalField(max_digits=8,decimal_places=2)
    pdescription=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.pname