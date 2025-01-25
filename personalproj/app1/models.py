from django.db import models

# Create your models here.
class logintable(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type=models.CharField(max_length=100)
    def __str__(self):
        return self.Name


class usertable(models.Model):
    Loginid = models.ForeignKey(logintable, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type = models.CharField(max_length=100)
    def __str__(self):
        return self. Name

class personaltable(models.Model):
    Name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    address=models.CharField(max_length=400)
    Email = models.EmailField()
    number = models.IntegerField()
    Type = models.CharField(max_length=150)
    def __str__(self):
        return self.Name

class educationtable(models.Model):
    Name = models.CharField(max_length=255)
    sslc_school = models.CharField(max_length=255)
    sslc_year = models.IntegerField()
    sslc_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    plus_two_school = models.CharField(max_length=255)
    plus_two_year = models.IntegerField()
    plus_two_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    degree_college = models.CharField(max_length=255)
    degree_course = models.CharField(max_length=255)
    degree_year = models.IntegerField()
    degree_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    Type = models.CharField(max_length=150)
    def __str__(self):
        return self.Name

class medicaltable(models.Model):
    Name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    height = models.FloatField(help_text="Height in centimeters")
    weight = models.FloatField(help_text="Weight in kilograms")
    blood_group = models.CharField(max_length=3)
    gender = models.CharField(max_length=10, help_text="Specify gender (e.g., Male, Female, Other)")
    allergies = models.TextField(blank=True, help_text="List any allergies")
    emergency_contact = models.CharField(max_length=100, help_text="Name and phone number")
    medications = models.TextField(blank=True, help_text="List current medications")

    def __str__(self):
        return self.Name


class accounttable(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Account Holder Name")
    bank_name = models.CharField(max_length=100, verbose_name="Bank Name")
    account_number = models.CharField(max_length=20, verbose_name="Account Number")
    ifsc_code = models.CharField(max_length=15, verbose_name="IFSC Code")
    account_type = models.CharField(max_length=50, verbose_name="Account Type")  # No predefined choices
    annual_income = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Total Annual Income")

    def __str__(self):
        return self.Name

class goaltable(models.Model):
    Name=models.CharField(max_length=1000)
    shortTermGoals=models.CharField(max_length=1000)
    longTermGoals= models.CharField(max_length=1000)
    dreamDestinations= models.CharField(max_length=1000)
    bucketListItems= models.CharField(max_length=1000)

    def __str__(self):
        return self.Name

