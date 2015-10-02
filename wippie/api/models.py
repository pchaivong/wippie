from django.contrib.auth.models import User
from django.db import models


# User profiles
# Extend django based User model
class UserProfile(User):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=16, null=True)
    avatar = models.URLField()
    birth = models.DateField()


# Holiday
# Contain holiday
class Holiday(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=56, null=True)

    def __unicode__(self):
        return "[%s] %s" % (self.date.strftime("%Y-%m-%d"), self.description)



