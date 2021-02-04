from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver



class Profile(models.Model):

    bio = HTMLField()
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  
    profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.user

    


class Neighbourhood(models.Model):
   
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'pic/', blank=False, null=False)
    description=models.TextField(max_length=100)
    bed_rooms=models.IntegerField(default='0')
    bath_rooms=models.IntegerField(default='0')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    admin=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    garage=models.IntegerField(default='0')

    def save_hood(self):
        self.save()

    def update_hood(self):
        self.update()

    def delete_hood(self):
        self.delete()

    
  


    @classmethod
    def search_by_title(cls,search_term):
        hood=cls.objects.filter(name__icontains=search_term)
        return hood

    def __str__(self):
        return self.name

    



class Business(models.Model):
    owner_name=models.CharField(max_length=40)
    owner_feedback=models.TextField(max_length=100)
    owner_email=models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, null=True,blank=True)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    def __str__(self):
        return self.owner_name


    @classmethod
    def search_by_title(cls,search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business


class Location(models.Model):
    
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()


class Post(models.Model):
    names=models.CharField(max_length=80)
    message=models.TextField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.names

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    @classmethod
    def get_post_by_hood(cls,id):
        post = Post.objects.filter(hood_id=id).all()
        return post

class Comment(models.Model):
    comment = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self):
        self.update()











