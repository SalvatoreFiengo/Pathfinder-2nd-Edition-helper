from django.contrib import admin
from .models import Anchestry, Ability, Heritage, Ancestry_feat, Ability_boost_flaw, Special_ability, Trait

# Register your models here.
admin.site.register(Ability)

class Ancestry_feat_Inline(admin.StackedInline):
    model = Ancestry_feat

class Ability_boost_flaw_Inline(admin.StackedInline):
    model = Ability_boost_flaw

class Heritage_Inline(admin.StackedInline):
    model = Heritage

class Special_ability_Inline(admin.StackedInline):
    model = Special_ability

class Trait_Inline(admin.StackedInline):
    model = Trait

class AnchestryAdmin(admin.ModelAdmin):
    inlines = [
        Heritage_Inline, Trait_Inline, Ability_boost_flaw_Inline, Ancestry_feat_Inline, Special_ability_Inline
    ]
admin.site.register(Anchestry, AnchestryAdmin)

