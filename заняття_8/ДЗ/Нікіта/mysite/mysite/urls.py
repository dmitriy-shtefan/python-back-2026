from django.contrib import admin
from django.urls import include, path, register_converter

from site_ui.translations import DEFAULT_LANG, LANGUAGES


class LangConverter:
    """Код языка в адресе: /uk/, /en/, ... (русский — без префикса)."""
    regex = '|'.join(code for code in LANGUAGES if code != DEFAULT_LANG)

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(LangConverter, 'lang')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Русская версия: адреса без префикса
    path('', include('pages.urls'), {'lang': DEFAULT_LANG}),
    # Остальные языки: /uk/, /en/, /de/, /fr/, /es/
    path('<lang:lang>/', include('pages.urls')),
]
