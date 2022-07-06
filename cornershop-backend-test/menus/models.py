import datetime
import uuid

from django.db import models
from django.urls import reverse


class Menu(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    menu_date = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("menus:menu-detail", kwargs={"id": self.id})


class MenuOption(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(
        "Menu",
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse("menus:menu-detail", kwargs={"id": self.menu.id})

    def __str__(self):
        return self.description
