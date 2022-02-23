
from email.policy import default
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.hashers import make_password

class MyAccountManager(BaseUserManager):
    def create_user(self, Email_Address, fullname=None, birthday=None, zipcode=None,password=None
                    ):
        if not Email_Address:
            raise ValueError('Users must have an email address')

        user = self.model(
            Email_Address=self.normalize_email(Email_Address),
            name=self.normalize_email(Email_Address),
            Date_of_Birth=birthday,
            zipcode=zipcode,
        )

        return user

    def create_superuser(self, Email_Address, password):
        user = self.create_user(
            Email_Address=self.normalize_email(Email_Address),
            password=password,
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
   
class Users(AbstractBaseUser,PermissionsMixin):
    Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    name = models.CharField(max_length=30, blank=True, null=True)
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    organization_admin = models.BooleanField(default=False)
    oganiztioncontroller = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email_Address'

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.Email_Address)


    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser


class Campaigns(models.Model):
    user = models.ForeignKey(
        Users, related_name="login_user", on_delete=models.CASCADE)
    
    Campaigns_id = models.CharField(max_length=20)
    Campaigns_name = models.CharField(max_length=30)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date  = models.DateTimeField(auto_now_add=True)


class Organization(models.Model):
    campaigns_name = models.CharField(max_length=20) 
    Organization_address = models.CharField(max_length=30)
    Organization_city = models.CharField(max_length=30)
    Organization_user = models.EmailField()
