from django.db import models
from django.utils.translation import gettext_lazy as _

from localflavor.us.models import USStateField
from django_countries.fields import CountryField

class CustomUser(models.Model):
    email = models.EmailField(_('Email'), unique=True)
    ip_address = models.GenericIPAddressField(_('IP Address'), blank=True, null=True)
    us_state = USStateField(_('US State'), null=True, blank=True)
    country = CountryField(_('Country'), null=True, blank=True)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.email