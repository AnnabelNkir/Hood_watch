from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    image = models.ImageField(upload_to = 'images/',null=True)
    occupants = models.IntegerField(null=True)
    police_dept = models.IntegerField(default='eg 999,269')
    health_dept = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True)
    objects = models.Manager()
    # Admin Foreign key
    def __str__(self):
        return self.name


    def save_neighbour(self):
        self.save()

    def delete_neighbour(self):
        self.delete()


    @classmethod
    def delete_neighbour_by_id(cls, id):
        neighbour = cls.objects.filter(pk=id)
        neighbour.delete()

    @classmethod
    def get_neighbour_by_id(cls, id):
        neighbour = cls.objects.get(pk=id)
        return neighbour

    @classmethod
    def filter_by_location(cls, location):
        neighbour = cls.objects.filter(location=location)
        return neighbour

    @classmethod
    def search_neighbour(cls, search_term):
        neighbour = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbour

    @classmethod
    def update_neighbour(cls, id):
        neighbour = cls.objects.filter(id=id).update(id=id)
        return neighbour

    @classmethod
    def update_neighbour(cls, id):
        neighbour = cls.objects.filter(id=id).update(id=id)
        return neighbour
   


# User class
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)
    bio = models.CharField(max_length =150,default='Hi, I am using neighbourhoodloop')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()

