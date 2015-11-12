from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from datetime import datetime

class TSUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(email,
                                password=password,
                                date_of_birth=date_of_birth)
        user.is_admin = True
        user.save(using=self._db)
        return user


class TSUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Personal info
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='profiles/', null=True)
    mobile = models.CharField(max_length=32, null=True)
    nickname = models.CharField(max_length=16, null=True)

    objects = TSUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.email

    def get_short_name(self):
        if self.nickname:
            return self.nickname
        return self.get_full_name()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# Holiday
# Contain holiday
class Holiday(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=56, null=True)

    def __unicode__(self):
        return "[%s] %s" % (self.date.strftime("%Y-%m-%d"), self.description)


# Wip
# Contain WIP Information daily

class Wip(models.Model):
    date = models.DateField()
    new_amt = models.PositiveSmallIntegerField()
    pending_amt = models.PositiveSmallIntegerField ()
    inprogress_amt = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return "[%s]" % (self.date.strftime("%Y-%m-%d"))

# Late

class Late(models.Model):
    date_id = models.OneToOneField(Wip, related_name="Late_Date", default=datetime.now)
    user_id = models.ForeignKey(TSUser, related_name="Late_User")


    def __unicode__(self):
        return "[%s] %s" % (self.date_id.date.strftime("%Y-%m-%d"), self.user_id.email)

# Leave
# TODO: Implement
class Leave(models.Model):
    date_id = models.OneToOneField(Wip, related_name="Leave_Date", default=datetime.now)
    user_id = models.ForeignKey(TSUser, related_name="Leave_User")
    duration = models.FloatField()

    def __unicode__(self):
        return "[%s] %s %.1f" % (self.date_id.date.strftime("%Y-%m-%d"), self.user_id.email, self.duration)

# OnCall

class OnCall(models.Model):
    date = models.DateField()
    shift_day = models.ForeignKey(TSUser, related_name="shift_day_username")
    shift_night = models.ForeignKey(TSUser, related_name="shift_night_username")
    queue_manager = models.ForeignKey(TSUser, related_name="queue_manager_username")

    def __unicode__(self):
        return "[%s] %s %s %s" % (self.date.strftime("%Y-%m-%d"), self.shift_day.email,
                                  self.shift_night.email, self.queue_manager.email)

