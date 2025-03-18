from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extrafields)
    
    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_staff', True)

        if extrafields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extrafields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extrafields)
    

class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=20)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    objects = UserManager()