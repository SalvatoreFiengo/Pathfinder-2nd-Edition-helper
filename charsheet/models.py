from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Ability(models.Model):
    name = models.CharField(blank=False, max_length=30)
    modifier = models.IntegerField(blank=False)
    score = models.IntegerField(blank=False)
    free = models.IntegerField(blank=False)
    def __str__(self):
        return self.name

@receiver(pre_save, sender=Ability)
def update_modifier(sender, instance, **kwargs):
    bonus = -5
    for n in range(0,instance.score):
        if n % 2:
            bonus += 1
    instance.modifier = bonus
    
    

class Anchestry(models.Model):
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=1500)
    hit_points = models.IntegerField(blank=False)
    size = models.CharField(blank=False, max_length=15)
    languages = models.CharField(blank=False, max_length=30)
    freeAbilities = models.IntegerField(blank=False)
    def __str__(self):
        return self.name

class Heritage(models.Model):
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=250)
    anchestry = models.ForeignKey(Anchestry, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Ancestry_feat(models.Model):
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=250)
    anchestry = models.ForeignKey(Anchestry, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class Ability_boost_flaw(models.Model):
    name = models.ForeignKey(Ability, on_delete=models.CASCADE)
    modifier = models.IntegerField(blank=False)
    anchestry = models.ForeignKey(Anchestry, on_delete=models.CASCADE)

class Trait(models.Model):
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=250)
    anchestry = models.ForeignKey(Anchestry, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Special_ability(models.Model):
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=250)
    anchestry = models.ForeignKey(Anchestry, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


