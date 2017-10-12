from django.db import models
from django.utils import timezone


# Create your models here.


class SlackUser(models.Model):
    bhawan_choices = (
        ('GB', 'Govind Bhawan'),
        ('KB', 'Kasturba Bhawan'),
        ('RB', 'Rajiv Bhawan'),
    )
    name = models.CharField(max_length=30)
    eno = models.IntegerField()
    uid = models.CharField(max_length=9, primary_key=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    email2 = models.EmailField(null=True)
    phone_no = models.CharField(max_length=20)
    phone_no_alt = models.CharField(max_length=20)
    room_no = models.CharField(max_length=7)
    bhawan = models.CharField(max_length=2, choices=bhawan_choices)
    # dob = models.DateField(default=timezone.now)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.eno) + '    ' + self.uid + '    ' + self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.email == self.email2:
            self.email2 = None

        super(SlackUser, self).save(force_insert=force_insert, force_update=force_insert, using=using,
                                    update_fields=update_fields)
