from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    BoardRollNo = models.CharField(max_length=50)
    RegistrationNo = models.CharField(max_length=50)
    InstituteRoll = models.CharField(max_length=50)
    Technology = models.CharField(max_length=50)
    Shift = models.CharField(max_length=50)
    Group = models.CharField(max_length=50)
    Session = models.CharField(max_length=50)
    FathersName = models.CharField(max_length=50)
    MothersName = models.CharField(max_length=50)
    Village = models.CharField(max_length=50)
    PostOffice = models.CharField(max_length=50)
    UpaZila = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    MobileNo = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.Name