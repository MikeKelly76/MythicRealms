from django.shortcuts import render, redirect
from django.utils.text import slugify
from . models import Character
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse
import datetime

@login_required(login_url="/users/login/")
def character_list(request): 
    characters = Character.objects.all().filter(owner=request.user).order_by('name') # geta all of the characters to load
    return render(request, 'characters/character_list.html', {'characters': characters})

@login_required(login_url="/users/login/")
def character_page(request, slug):
    character = Character.objects.get(slug=slug)
    modifiers = []
    modifiers.append(calc_modifier(character.dex, character.acrobatics))
    modifiers.append(calc_modifier(character.wis, character.animal_handling))
    modifiers.append(calc_modifier(character.int, character.arcana))
    modifiers.append(calc_modifier(character.str, character.athletics))
    modifiers.append(calc_modifier(character.cha, character.deception))
    modifiers.append(calc_modifier(character.int, character.history))
    modifiers.append(calc_modifier(character.wis, character.insight))
    modifiers.append(calc_modifier(character.cha, character.intimidation))
    modifiers.append(calc_modifier(character.int, character.investigation))
    modifiers.append(calc_modifier(character.wis, character.medicine))
    modifiers.append(calc_modifier(character.wis, character.nature))
    modifiers.append(calc_modifier(character.wis, character.perception))
    modifiers.append(calc_modifier(character.cha, character.performance))
    modifiers.append(calc_modifier(character.cha, character.persuasion))
    modifiers.append(calc_modifier(character.int, character.religion))
    modifiers.append(calc_modifier(character.dex, character.sleight_of_hand))
    modifiers.append(calc_modifier(character.dex, character.stealth))
    modifiers.append(calc_modifier(character.wis, character.survival))
    return render(request, 'characters/character_page.html', {'character': character, 'modifiers': modifiers})

def calc_modifier(att, prof):
    if (prof):
        temp = int((att - 10)/ 2 + 2)
    else:
        temp = int((att - 10) / 2)
    if (temp >= 0):
        return (f'+{temp}')
    else:
        return (f'{temp}')

@login_required(login_url="/users/login/")
def new_character(request):
    if request.method == "POST":
        form = forms.CreateCharacter(request.POST, request.FILES)
        if form.is_valid():
            newCharacter = form.save(commit=False)
            newCharacter.owner = request.user
            newCharacter.save()
            return redirect("characters:list")
    else:
        form = forms.CreateCharacter()
    return render(request, 'characters/new-character.html', { 'form': form })
