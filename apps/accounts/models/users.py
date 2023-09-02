from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_verified = models.BooleanField(
        verbose_name=_('email verified'),
        default=False,
        help_text=_('Designates if this user email has been verified.'),
    )

    # overwritten to remove the useless `username` field from database
    username = models.CharField(
        verbose_name=_('username'),
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self) -> str:
        return f'{self.phone}-{self.first_name}-{self.last_name}'
