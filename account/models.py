from distutils.log import error
from enum import auto, unique
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email = self.normalize_email(email),
            username=username,

        )
       

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using =self._db)
        return user


      

class User(AbstractBaseUser):
    
        

        first_name = models.CharField(max_length = 20)
        last_name = models.CharField(max_length = 20)
        email = models.EmailField(max_length = 200 ,unique = True)
        username = models.CharField(max_length = 20 , unique = True)
        phone_number =  models.CharField(max_length = 13 ,unique= True, null = True, blank= True )
        



        date_joined = models.DateTimeField(auto_now_add = True)
        last_login = models.DateTimeField(auto_now_add = True)
        created_date = models.DateTimeField(auto_now_add = True)
        modified_date = models.DateField(auto_now_add = True)
        is_admin = models.BooleanField(default = False)
        is_active = models.BooleanField(default = False)
        is_staff = models.BooleanField(default = False)
        is_superadmin = models.BooleanField(default = False)    

        objects = UserManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username','first_name','last_name','password']

        class Meta: 
            verbose_name_plural = "Users"


        def __str__(self):
            return self.email

        def has_perm(self,perm,obj = None):
            return self.is_admin

        def has_module_perms(self,app_label):
            return True
