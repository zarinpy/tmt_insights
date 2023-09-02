from typing import TypeVar

from django.db import models
from django.contrib import admin

_ModelT = TypeVar("_ModelT", bound=models.Model)


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 25
    actions_on_top = True
    actions_on_bottom = True
