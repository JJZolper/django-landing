from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(models.Model):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.email