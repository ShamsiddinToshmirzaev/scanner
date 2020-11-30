from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField
from mptt.models import MPTTModel, TreeForeignKey


class Target(models.Model):
    target = models.CharField(max_length=255)
    type = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.target


class Scan_Type(MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey("self", default=None, blank=True, null=True, on_delete=models.CASCADE,
                            related_name='children')
    command = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Scan Types'

    def __str__(self):
        return self.name


class Scan(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    FINISHED = 'finished'
    STATUS = [
        (ACTIVE, ('Active')), (INACTIVE, ('Inactive')), (FINISHED, ('Finished'))
    ]
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    scan_type = models.ForeignKey(Scan_Type, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    finish_date = models.DateTimeField(blank=True)
    status = models.CharField(max_length=32, choices=STATUS, default=INACTIVE)
    progress = models.FloatField(blank=True, null=True)
    command = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.target.target


class Result(models.Model):
    xml = JSONField(null=True)
    json = JSONField(null=True)
