from django.db import models
from django.utils.translation import ugettext_lazy as _

from authtools.models import AbstractNamedUser

class User(AbstractNamedUser):
    class Meta:
        db_table = 'auth_user'
