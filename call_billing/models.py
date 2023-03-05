from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Call(BaseModel):
    user_name = models.CharField(db_index=True, max_length=32)
    call_duration = models.IntegerField()

    class Meta:
        db_table = "calls"
