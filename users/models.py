from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.backends import ModelBackend


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=250, default=' ', blank=True)

    def __str__(self):
        return "{}'s Profile".format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(email__iexact=username) | Q(username__iexact=username))
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
