from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def ValidateFirstCapitalLetter(firstName: str):
    if not 65 <= ord(firstName[0]) <= 90:
        raise ValidationError('Your name must start with a capital letter!')


def ValidateOnlyLetters(name: str):
    if len([char for char in name if not char.isalpha()]) > 0:
        print([char for char in name if char.isalpha()])
        raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    firstName = models.CharField(max_length=20, validators=[ValidateFirstCapitalLetter])
    lastName = models.CharField(max_length=20, validators=[ValidateFirstCapitalLetter])
    profilePicture = models.URLField(null=True, blank=True)


class Plant(models.Model):
    plantType = models.CharField(max_length=14, choices=(('outdoor', 'Outdoor Plants'), ('indoor', 'Indoor Plants')))
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), ValidateOnlyLetters])
    imageUrl = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    plantOwner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=True, blank=True)

# delete last migration

# Deleting a profile should delete the profile info and all of his /her added plants.