from django import forms

from .models import Item


class LostItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "date")
        labels = {
            "name": "Назва речі",
            "place": "Місце втрати",
            "date": "Дата втрати",
        }
        help_texts = {"date": "Формат РРРР-ММ-ДД, наприклад 2026-11-20."}
