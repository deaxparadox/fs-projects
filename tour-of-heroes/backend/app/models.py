from django.db import models

class HeroModel(models.Model):
    hero_id = models.IntegerField()
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name