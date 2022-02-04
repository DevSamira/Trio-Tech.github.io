from django.db import models
from django.conf import settings

from apps.base_app.models import BaseModel


USER = settings.AUTH_USER_MODEL


class Order(BaseModel):

    STATUS_CHOICES = (
        (0, "Pendente"),
        (1, "Aceito"),
        (2, "Rejeitado")
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    owner = models.ForeignKey(USER, on_delete=models.CASCADE)

    @property
    def get_status(self):
        return self.STATUS_CHOICES[self.status][1]

    def __str__(self):
        return self.title
