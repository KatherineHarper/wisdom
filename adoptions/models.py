from django.db import models
import logging
from django.contrib.auth.signals import user_login_failed

from django.dispatch import receiver
log = logging.getLogger(__name__)

# log failed login and user name to identify brute force attacks
@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    log.warning('login failed for: {credentials}'.format(
        credentials=credentials['username'],
    ))
#
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
