from django.db import models

# Create your models here.

class Information(models.Model):
    First_Name = models.CharField(max_length = 100, primary_key = True)
    Middle_Name = models.CharField(max_length = 100, blank = True)
    Father_Name = models.CharField(max_length = 100)
    Mother_Name = models.CharField(max_length = 100)
    Current_Address = models.TextField()
    Permanent = models.TextField()
    Phone_number = models.IntegerField(unique = True)
    Land_line = models.IntegerField(blank = True)
    Date_of_Birth = models.DateField(auto_now_add=True)
    Place_of_Birth = models.DateField(blank = True)
    
    def __str__(self):
        return self.First_Name

