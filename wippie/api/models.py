from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


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
# TODO: Implement
class Wip(models.Model):
    pass


# Late
# TODO: Implement
class Late(models.Model):
    pass


# Leave
# TODO: Implement
class Leave(models.Model):
    pass


# OnCall
# TODO: Implement
class OnCall(models.Model):
    pass



