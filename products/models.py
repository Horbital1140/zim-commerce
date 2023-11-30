from django.db import models


class product_details(models.Model):
    name = models.CharField (max_length=255)
    price = models.FloatField ()
    stock = models.IntegerField ()
    image = models.CharField (max_length=2083)
    description = models.CharField (max_length=2083)

class funding(models.Model):
    email = models.CharField (max_length=255)
    amount = models.FloatField ()
    

class offer(models.Model):
    code = models.CharField (max_length=255)
    description = models.CharField (max_length=2083)
    discount = models.FloatField ()


class department(models.Model):
     unit = models.CharField (max_length= 255)
     grade = models.CharField (max_length=255)


