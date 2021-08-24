from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError('Users must have an username')
        user=self.model(username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,username,password):
        user=self.create_user(username=username,password=password)
        user.is_admin=True
        user.save(using=self.db)
        return user

class labUser(AbstractBaseUser,PermissionsMixin):
    id=models.BigAutoField(primary_key=True)
    username=models.CharField('Name',max_length=15,unique=True)
    password=models.CharField('Password',max_length=256)
    objects=UserManager()

    USERNAME_FIELD='username'

class Laboratorio(models.Model):
    ESTADO_LABORATORIO=(
        ("M","En Mantenimiento"),
        ("D","Disponible"),
    )
    lab_id=models.BigAutoField(primary_key=True)
    categoria=models.CharField('Categoria',max_length=100)
    descripcion=models.CharField('Descripcion',max_length=100)
    ubicacion=models.CharField('Ubicacion',max_length=100)
    estado=models.CharField('Estado',max_length=100,choices=ESTADO_LABORATORIO)
    aforo=models.IntegerField('Aforo')


# Create your models here.
