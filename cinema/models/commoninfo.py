# -*- coding: utf-8 -*-

"""cinema: common information."""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cinema.models import constants


class CommonInfo(models.Model):

    """Common information."""

    country = models.CharField(_("country"), max_length=2, choices=constants.COUNTRY_CHOICES, help_text=_("Country."))

    class Meta:
        abstract = True
