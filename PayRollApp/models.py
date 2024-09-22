from django.db import models

class Employee(models.Model):
    COUNTRIES=[
        ("PAK", "PAKISTAN"),
        ("IND", "INDIA"),
        ("USA", "United States Of America"),
        ("AUS", "AUSTRALIA"),
        ("AU", "AUSTRIA"),
        ("UAE", "United Arab Emirates"),
    ]

    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    TitleName = models.CharField(max_length=30)
    HasPassport = models.BooleanField()
    Salary = models.IntegerField()
    BirthDate = models.DateField()
    HireDate= models.DateField()
    Notes = models.CharField(max_length=200)
    Country=models.CharField(max_length=35, choices=COUNTRIES,default=None)
    Email = models.EmailField(default="", max_length=50)
    PhoneNumber = models.CharField(default="", max_length=20)

    