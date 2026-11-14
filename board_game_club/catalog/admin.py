from django.contrib import admin

from .models import BoardGame


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ("title", "max_players", "is_available")
