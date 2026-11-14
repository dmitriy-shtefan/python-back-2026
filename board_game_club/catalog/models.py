from django.db import models


class BoardGame(models.Model):
    title = models.CharField(max_length=100)
    max_players = models.PositiveSmallIntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        return self.title
