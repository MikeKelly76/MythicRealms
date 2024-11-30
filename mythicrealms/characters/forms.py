from django import forms
from . import models

ANCESTRY_CHOICES = [
    ('')
]

class CreateCharacter(forms.ModelForm):
    class Meta:
        model = models.Character
        fields = ['name', 'ancestry', 'background', 'ch_class', 'ch_image', 'str', 'dex', 'con', 'int', 'wis', 'cha', 'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 'history', 'insight', 'intimidation', 'investigation', 'medicine', 'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 'stealth', 'survival', 'slug']