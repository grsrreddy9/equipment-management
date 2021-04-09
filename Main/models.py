from django.db import models

# Create your models here.
class Manufacturer(models.Model):
 name=models.CharField(max_length=100)

class Department(models.Model):
 name=models.CharField(max_length=100)

class Product(models.Model):
 product_name= models.CharField(max_length=100)
 product_code=models. CharField(max_length=10)
 product_strength = models.CharField(max_length=10)



class Equipment(models.Model):
 equipment_name= models.CharField(max_length=100)
 equipment_id= models.CharField(max_length=20)
 equipment_capacity= models.IntegerField()
 equipment_model= models.CharField(max_length=100)
 department= models.ForeignKey(Department, on_delete=models.CASCADE)
 manufacturer= models.ForeignKey(Manufacturer, on_delete=models.CASCADE)







