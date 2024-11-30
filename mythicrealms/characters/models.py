from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length= 50)
    ancestry = models.CharField(max_length= 50)
    background = models.CharField(max_length= 50)
    ch_class = models.CharField(max_length= 50)
    ch_image = models.ImageField(default='fallback.png', blank=True)
    str = models.IntegerField()
    dex = models.IntegerField()
    con = models.IntegerField()
    int = models.IntegerField()
    wis = models.IntegerField()
    cha = models.IntegerField()
    acrobatics = models.BooleanField()
    animal_handling = models.BooleanField()
    arcana = models.BooleanField()
    athletics = models.BooleanField()
    deception = models.BooleanField()
    history = models.BooleanField()
    insight = models.BooleanField()
    intimidation = models.BooleanField()
    investigation = models.BooleanField()
    medicine = models.BooleanField()
    nature = models.BooleanField()
    perception = models.BooleanField()
    performance = models.BooleanField()
    persuasion = models.BooleanField()
    religion = models.BooleanField()
    sleight_of_hand = models.BooleanField()
    stealth = models.BooleanField()
    survival = models.BooleanField()
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name