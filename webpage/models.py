from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    phone = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=20,blank=True)
    zipcode =models.CharField(max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender , instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender =User)


class breed(models.Model):

    ACTIVITY_LEVEL_CHOICES = [ ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ] 
    SIZE_CHOICES = [ ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ]


    name = models.CharField(max_length=50)
    good_with_kids = models.BooleanField(default=False)
    low_shedding =models.BooleanField(default=False)
    first_time_owner = models.BooleanField(default=False)
    Guard_dog = models.BooleanField(default=False)
    athletic = models.BooleanField(default=False)
    first_time_owner = models.BooleanField(default=False)
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_LEVEL_CHOICES, default='medium')
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='medium')
    


    def __str__(self):
        return self.name
    

    

class pet(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=20)
    breed=models.ForeignKey(breed,on_delete=models.CASCADE,default=1)
    gender=models.CharField(max_length=10,)
    description = models.TextField(max_length=300,blank=True)
    size=models.TextField(max_length=20)
    vaccinations = models.BooleanField(default=False)
    spayed_neutered = models.BooleanField(default=False)
    medical_conditions = models.CharField(max_length=100, blank=True)
    image=models.ImageField(upload_to=("upload/image/"))
    is_adopted=models.BooleanField(default=False)

    

    def __str__(self): 
        return self.name
    
    class Meta:
        permissions = [("can_add_pet","can add pet")]
    
    

    
class adoption(models.Model):
    pet =models.ForeignKey(pet,on_delete=models.CASCADE,default=1)
    customer =models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    address =models.CharField(max_length=100)
    phone =models.CharField(max_length=15)
    city = models.CharField(max_length=20,blank=True)
    state = models.CharField(max_length=20,blank=True)
    zipcode =models.CharField(max_length=15,blank=True)
    declaration =models.BooleanField(default=False)
    date =models.DateField(default=datetime.datetime.today)
    status =models.BooleanField(default=False)


    def __str__(self): 
        return f"Adoption of {self.pet.name} by {self.customer.username}"


# Create your models here.
