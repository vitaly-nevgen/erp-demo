from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _

from core.consts import EMPLOYEE_GROUP_NAME


class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('phone number'))
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('position'))
    supervisor = models.ForeignKey(
        'self', models.CASCADE, blank=True, null=True,
        related_name='subordinates', verbose_name=_('supervisor'),
    )

    def save(self, *args, **kwargs):
        creating = False
        if not self.pk:
            creating = True
            self._password = self.password
        super().save(*args, **kwargs)

        if creating:
            employee_group = Group.objects.get(name=EMPLOYEE_GROUP_NAME)
            self.groups.add(employee_group)

    def __str__(self):
        return f'User {self.username}'

    class Meta:
        permissions = (
            ("view_structure", _("Can view organization structure")),
            ("view_own_subordinates", _("Can view own subordinates")),
            ("view_own_supervisor", _("Can view own supervisor")),
            ("change_user_subordinates", _("Can change user subordinates")),
            ("change_user_supervisor", _("Can change user supervisor")),
        )
