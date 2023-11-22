from django.db import models

class HeroModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name