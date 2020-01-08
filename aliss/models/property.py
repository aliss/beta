import uuid
from django.db import models
from django.utils.html import format_html


class Property(models.Model):
    class Meta:
        verbose_name_plural = "properties"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    icon = models.CharField(max_length=100, default="fa fa-circle")
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=140, null=False, blank=False)
    for_organisations = models.BooleanField(default=True)
    for_services      = models.BooleanField(default=True)
    for_locations     = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def icon_html(self):
        return format_html('<i class="{}" aria-hidden="true"></i>', self.icon)
