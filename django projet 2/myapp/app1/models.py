from django.db import models
from django.contrib.auth.hashers import make_password

class Register(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Şifreyi kaydetmeden önce hashle
        if self.password:
            self.password = make_password(self.password)
        super(Register, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name



