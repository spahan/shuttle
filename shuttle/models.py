from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.crypto import get_random_string
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Car(models.Model):
    title = models.CharField(max_length=20)
    space = models.IntegerField(default=3)

    def __str__(self):
        return '{0} ({1})'.format(self.title,self.space)

class Driver(models.Model):
    nick = models.CharField(max_length=20)
    phone = PhoneNumberField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    token = models.CharField(max_length=12, default=get_random_string, editable=False)
    def __str__(self):
        return self.nick

class Shuttle(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    departure = models.DateTimeField()
    route = models.URLField(null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return '{0} | {1}'.format(self.title, self.departure.strftime('%d-%H:%M'))

class Passenger(models.Model):
    nick = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    mail = models.EmailField(blank=True, null=True)
    token = models.CharField(max_length=12, default=get_random_string, editable=False)
    shuttle = models.ForeignKey(Shuttle, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} on {1}'.format(self.nick,self.shuttle)
