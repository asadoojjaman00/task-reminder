from django.contrib.auth.models import BaseUserManager
import uuid

class UserManager(BaseUserManager):
    def create_user(self,full_name, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError("user must have an email address")
        
        email = self.normalize_email(email)

        username = email.split('@')[0] + str(uuid.uuid4())[:4]
        user = self.model(
            full_name=full_name,
            username=username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using= self._db)
        
        return user
    

    def create_superuser(self,full_name,  email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser = True')
        

        return self.create_user(full_name,  email, password, **extra_fields)
    