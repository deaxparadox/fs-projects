from django.contrib import admin

from .models import HeroModel


class HeroAdmin(admin.ModelAdmin):
    pass 

admin.site.register(HeroModel, HeroAdmin)