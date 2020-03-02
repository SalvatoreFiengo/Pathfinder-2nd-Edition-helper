from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Anchestry, Heritage, Ability, Ability_boost_flaw, Trait

def charsheet(request):
    abilities = Ability.objects.all()
    anchestries = Anchestry.objects.all()
    return render(request, "charsheet.html", {"abilities":abilities, "anchestries":anchestries})

def add_anchestry(request):
    abilities = Ability.objects.all()
    anchestries = Anchestry.objects.all()
    if request.method == "POST" and request.POST["anchestry"] != "none":
        heritages = Heritage.objects.all()
        traits = Trait.objects.all()
        pk = request.POST["anchestry"]
        selected_anchestry = Anchestry.objects.get(pk=pk)
        
        bonuses = Ability_boost_flaw.objects.all()
        for ability in abilities:
            ability.score = 10
            ability.save()
            for bonus in bonuses:
                if bonus.anchestry.id == selected_anchestry.id and bonus.name.id == ability.id:
                    ability.score = ability.score + bonus.modifier
                    ability.save()
        updated_abilities = Ability.objects.all()
        return render(request, "charsheet.html", 
            {"abilities":updated_abilities, 
            "anchestries":anchestries, 
            "sel_anchestry":selected_anchestry.name,
            "heritages":heritages,
            "size":selected_anchestry.size,
            "traits":traits,
            "free":selected_anchestry.freeAbilities})
    else:
        for ability in abilities:
            ability.score = 10
            ability.save()
        return render(request, "charsheet.html", {"abilities":abilities, "anchestries":anchestries})        

def anchestries(request):
    anchestries = Anchestry.objects.all()
    heritages = Heritage.objects.all()
    return render(request, "anchestry.html", { "anchestries":anchestries, "heritages":heritages })
