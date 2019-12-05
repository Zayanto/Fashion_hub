from django.db import models

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    address = models.TextField()



class men_dress(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='media',blank=True)
    image2 = models.ImageField(upload_to='media',blank=True)
    image3 = models.ImageField(upload_to='media',blank=True)
    image4 = models.ImageField(upload_to='media',blank=True)
    image5 = models.ImageField(upload_to='media',blank=True)


class women_dress(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='media',blank=True)
    image2 = models.ImageField(upload_to='media',blank=True)
    image3 = models.ImageField(upload_to='media',blank=True)
    image4 = models.ImageField(upload_to='media',blank=True)
    image5 = models.ImageField(upload_to='media',blank=True)


class boys_dress(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='media',blank=True)
    image2 = models.ImageField(upload_to='media',blank=True)
    image3 = models.ImageField(upload_to='media',blank=True)
    image4 = models.ImageField(upload_to='media',blank=True)
    image5 = models.ImageField(upload_to='media',blank=True)


class girls_dress(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='media',blank=True)
    image2 = models.ImageField(upload_to='media',blank=True)
    image3 = models.ImageField(upload_to='media',blank=True)
    image4 = models.ImageField(upload_to='media',blank=True)
    image5 = models.ImageField(upload_to='media',blank=True)
    image6 = models.ImageField(upload_to='media',blank=True)


class check_out(models.Model):
    name = models.CharField(max_length=500)
    address = models.TextField()
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='media',blank=True)
    full_name = models.CharField(max_length=500)
    mobile = models.BigIntegerField(default=0)
    landmark = models.CharField(max_length=500)
   
    address_type = models.TextField(blank=True)


class order(models.Model):
    username = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    mobile = models.BigIntegerField(default=0)
    landmark = models.CharField(max_length=500)
    address = models.TextField()
    address_type = models.TextField()
    #items = models.ForeignKey(check_out, blank = True, on_delete=models.CASCADE,default = 0)
    
    