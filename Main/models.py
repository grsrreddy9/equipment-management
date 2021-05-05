import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=10)
    product_strength = models.CharField(max_length=10)


class Equipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment_name = models.CharField(max_length=100)
    equipment_id = models.CharField(max_length=20)
    equipment_capacity = models.IntegerField()
    equipment_model = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=10)


class ProductGranulation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    batch_number = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    equipment = models.ManyToManyField(Equipment)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
