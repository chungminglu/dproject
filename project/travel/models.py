from django.db import models

# Create your models here.
class site(models.Model):
    ID = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Address = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    URL = models.CharField(max_length=60, null=False)

    def __str__(self):		
        return self.Name

class gthoteltime(models.Model):
    Id = models.CharField(max_length=10, null=False)
    ChiName = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    CheckIn = models.CharField(max_length=20, null=False)
    CheckOut = models.CharField(max_length=20, null=False)
    Score = models.DecimalField(max_digits=6,decimal_places=3,null=False)

    def __str__(self):		
        return self.ChiName

class gtsitactivity(models.Model):
    Id = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    Score = Score = models.DecimalField(max_digits=6,decimal_places=3 ,null=False)

    def __str__(self):		
        return self.Name

class  gtsiteapparel(models.Model):
    Id = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    Score = Score = models.DecimalField(max_digits=6,decimal_places=3,null=False)

    def __str__(self):		
        return self.Name

class gtsiteother(models.Model):
    Id = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    Score = Score = models.DecimalField(max_digits=6,decimal_places=3,null=False)

    def __str__(self):		
        return self.Name

class gtsiterestaurant(models.Model):
    Id = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    Score = Score = models.DecimalField(max_digits=6,decimal_places=3,null=False)

    def __str__(self):		
        return self.Name

class gtsiteshop(models.Model):
    Id = models.CharField(max_length=10, null=False)
    Name = models.CharField(max_length=60, null=False)
    Lat = models.CharField(max_length=20, null=False)
    Lng = models.CharField(max_length=20, null=False)
    Score = Score = models.DecimalField(max_digits=6,decimal_places=3,null=False)

    def __str__(self):		
        return self.Name
    
