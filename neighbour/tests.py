from django.test import TestCase
from .models import Neighbour,Profile,Post,Business
from django.contrib.auth.models import User

# Create your tests here.

class NeighbourTestClass(TestCase):

    def setUp(self):
        self.Nei= Neighbour(name = 'Bella', location='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nei,Neighbour))


    def test_save_method(self):
        self.Nei.save_neighbour()
        neighbour = Neighbour.objects.all()
        self.assertTrue(len(neighbour) > 0)

    def test_data(self):
        self.assertTrue(self.Nei.name,"Kenya")


    def test_delete(self):
        hood = Neighbour.objects.filter(id=1)
        hood.delete()
        hoods = Neighbour.objects.all()
        self.assertTrue(len(hoods)==0)

    def test_get_hood_by_id(self):
        self.Nei.save()
        hoods = Neighbour.objects.get(id=1)
        self.assertTrue(hoods.name,'stayville')


class ProfileTestClass(TestCase):

    def setUp(self):
        self.Pro= Profile(name = 'Jeff', bio='Made with love')
        self.new_user=User(username='aa',first_name='a',last_name='a',email='a@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,bio='YOH')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Profile))

    def test_save_method(self):
        self.Pro.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Profile.objects.filter(id=1)
        post.delete()
        posts = Profile.objects.all()
        self.assertTrue(len(posts)==0)

    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='MIMI').update(bio = 'Me')
        self.updated_profile = Profile.objects.get(bio='Me')
        self.assertTrue(self.updated_profile.bio,'Me')

class PostTestClass(TestCase):

    def setUp(self):
        self.Pos= Post(post='School recommendations')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pos,Post))

    def test_save_method(self):
        self.Pos.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_data(self):
        self.assertTrue(self.Pos.post,"test")

    def test_delete(self):
        post = Post.objects.filter(id=1)
        post.delete()
        posts = Post.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Pos.save()
        posts = Post.objects.get(id=1)
        self.assertTrue(posts.post,'kol')



class BusinessTestClass(TestCase):

    def setUp(self):
        self.Bus= Business(name = 'Groceries', description='Vitu freshi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Bus,Business))


    def test_save_method(self):
        self.Bus.save_biz()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_data(self):
        self.assertTrue(self.Bus.name,"Groceries")


    def test_delete(self):
        biz = Business.objects.filter(id=1)
        biz.delete()
        bizs = Business.objects.all()
        self.assertTrue(len(bizs)==0)

    def test_get_biz_by_id(self):
        self.Bus.save()
        bizs = Business.objects.get(id=1)
        self.assertTrue(bizs.name,'stayville')