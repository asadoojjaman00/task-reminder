from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,full_name, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("user must have an username")
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)

        user = self.model(
            full_name=full_name,
            username=username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using= self._db)
        
        return user
    

    def create_superuser(self,full_name, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(full_name, username, email, password, **extra_fields)
    