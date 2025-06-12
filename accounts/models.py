from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.

class User(models.Model):
    FREE ='free'
    FREEMIUM='freemium'

    ACCESS_TYPE_CHOICES =[
        (FREE,'Free'),
        (FREEMIUM,'Freemium'),

    ]

    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    access_type=models.CharField(max_length=10,choices=ACCESS_TYPE_CHOICES,default=FREE)

    def set_password(self, raw_password):
        self.password=make_password(raw_password)

    def check_password(self,raw_passsword):
        return check_password(raw_passsword,self.password)

    def __str__(self):
        return self.email  
