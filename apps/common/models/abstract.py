import uuid

from django.db import models
from django.conf import settings
from django.utils import text
from django.utils.translation import gettext_lazy as _


class SoftDeleteModelMixin(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('is deleted'),
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('deleted at'),
    )

    class Meta:
        abstract = True


class UserModelMixin(models.Model):
    """
    Abstract base class for models that have a user as a foreign key.
    """

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class UniversalModelMixin(models.Model):
    """Universal primary key mixin

    This mixin changes the primary key of a model to UUID field.
    Using UUID as primary key could help application scalability
    and could make migrating to micro-service, or exporting or
    importing data easier,
    by using a universally unique identifier
    for object that without fear of collision.
    """

    id = models.UUIDField(
        verbose_name=_("universal unique id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("Universally unique object identifier"),
    )

    class Meta:
        abstract = True

    @property
    def serial(self) -> str:
        return str(self.id).upper().split("-")[0]

    def __str__(self):
        return self.serial


class TimestampedModelMixin(models.Model):
    """Timestamp mixin

    This mixin adds a timestamp to model for create and update events
    """

    created = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("This is the timestamp of the object creation."),
    )
    updated = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_("This is the timestamp of the object update"),
    )

    class Meta:
        ordering = ["-created"]
        abstract = True


class ActivatedModelManager(models.Manager):
    def actives(self):
        return self.get_queryset().filter(is_active=True)


class PublishedModelManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published=True)


class PublishedModelMixin(models.Model):
    is_published = models.BooleanField(
        verbose_name=_("is published"),
        default=True,
        db_index=True
    )

    class Meta:
        abstract = True


class ActivatedModelMixin(models.Model):
    """Active objects mixin

    This mixin add a is_active field to the model
    which indicated the model active status.
    It also adds a queryset to support
    getting only active objects.
    """

    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        db_index=True,
        help_text=_(
            "Designates if this object should be considered active or not "
            "or to simulate soft delete behaviour."
        ),
    )

    objects = ActivatedModelManager()

    class Meta:
        abstract = True
