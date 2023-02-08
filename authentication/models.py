
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self,user_name,email,age,sex,role, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not user_name:
            raise ValueError("afasdfa")

        user = self.model(
            user_name = user_name,
            email= email,
            age=age,
            sex = sex,
            role = role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,user_name, email,age,sex,role, password=None):
        user = self.create_user(
            user_name = user_name,
            email= email,
            age=age,
            sex = sex,
            role = role,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255,unique=True)
   
    age = models.IntegerField(default=0)
    sex_choice = ((0,'Nữ'),(1,"Nam"),(2,"Khác"))
    sex = models.IntegerField(sex_choice,default=0)
    role_choice = ((0,"User"),(1,"Admin"))
    role = models.BooleanField(role_choice,default=0)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email','age','sex','role']
    objects = MyUserManager()

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True