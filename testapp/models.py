from django.db import models
from django.contrib.auth.models import User


class UserWeightModel(models.Model):
    user_id = models.ForeignKey(
        User,
        related_name="user_id",
        db_column='_id',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    weight = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
