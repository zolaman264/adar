from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

position_choice={
    ('Lobby 1','Lobby 1'),
    ('Lobby 2','Lobby 2'),
    ('Loading dock','Loading dock'),
    ('Patrol 1','Patrol 1'),
    ('Patrol 2','Patrol 2'),
}
# Create your models here.
class Post(models.Model):
    report_image=models.ImageField(null=True,blank=True, upload_to='images/')
    checkin=models.TimeField(max_length=200)
    checkout=models.TimeField(max_length=200)
    position=models.CharField(max_length=200,choices=position_choice)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    details=RichTextField(blank=True,null=True)
    report=RichTextField(blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.author.first_name ) 
    def get_absolute_url(self):
        return reverse('home') 
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio =models.TextField()
    profile_pic=models.ImageField(null=True,blank=True, upload_to='images/profile/')
    def __str__(self):
        return str(self.user) 
