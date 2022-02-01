from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit import models as image_models
from imagekit import processors as image_proc


class User(AbstractUser):

    picture = models.ImageField(
        upload_to='accounts/%Y/%m/%d', null=False, blank=True)

    picture_thumb = image_models.ImageSpecField(source='picture', processors=[
        image_proc.ResizeToFit(200, 200)], format='JPEG', options={'quality': 60})
