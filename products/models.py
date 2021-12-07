from django.db import models
from enum import Enum

class Laptoptable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    hd_capacity = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptop'

class Mobiletable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    screen_size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile'

class Producttable(models.Model):
    class categorySelect(Enum):
        Laptop = ('L', 'Laptop')
        Mobile = ('M', 'Mobile')
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=10, choices=[x.value for x in categorySelect])
    processor = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    laptop = models.ForeignKey(Laptoptable, models.DO_NOTHING, blank=True, null=True)
    mobile = models.ForeignKey(Mobiletable, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
