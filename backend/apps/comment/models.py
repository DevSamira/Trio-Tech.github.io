from django.db import models
from django.conf import settings

from apps.base_app.models import BaseModel
from apps.order.models import Order

USER = settings.AUTH_USER_MODEL


class Comment(BaseModel):

    comment = models.TextField()
    owner = models.ForeignKey(USER, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:15] + "..."
