import uuid

from django.db import models
from django.urls import reverse

from menus.models import MenuOption


class MenuSelection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee_firstname = models.CharField(max_length=128)
    employee_lastname = models.CharField(max_length=128)
    employee_id = models.IntegerField()
    selection = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    extra_large = models.BooleanField(default=False)
    specification = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("menuselections:menuselection-detail", kwargs={"id": self.id})
