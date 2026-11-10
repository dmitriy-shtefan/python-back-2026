from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render

from site_ui.translations import DEFAULT_LANG, TEXTS

# Заготовка онлайн-казино (игровые фишки, без реальных денег).
# Названия и описания игр лежат в site_ui/translations.py (game_names, game_descriptions).
GAMES = {
    1: {'related': [2, 3], 'added': date(2026, 4, 25)},
    2: {'related': [1], 'added': date(2026, 5, 10)},
    3: {'related': [], 'added': date(2026, 6, 1)},
}


def prefix(lang):
    return '' if lang == DEFAULT_LANG else f'/{lang}'


def page(request, title, text, status=200, cta=None, cta_url='/'):
    return render(request, 'pages/page.html', {
        'title': title, 'text': text,
        'cta': cta, 'cta_url': cta_url,
    }, status=status)


def home(request, lang):
    t = TEXTS[lang]
    games = [{'id': i, 'title': name} for i, name in enumerate(t['game_names'], start=1)]
    return render(request, 'pages/home.html', {'games': games})


def about(request, lang):
    t = TEXTS[lang]
    return page(request, t['about_title'], t['about_text'])


def contacts(request, lang):
    t = TEXTS[lang]
    return page(request, t['contacts_title'], t['contacts_text'])


def detail(request, lang, pk):
    t = TEXTS[lang]
    game = GAMES.get(pk)
    if game is None:
        return page(request, t['not_found_title'], t['not_found_text'],
                    status=404, cta=t['to_home'], cta_url=prefix(lang) + '/')
    context = {
        'game': {
            'id': pk,
            'title': t['game_names'][pk - 1],
            'description': t['game_descriptions'][pk - 1],
            'added': game['added'],
        },
        'related': [{'id': i, 'title': t['game_names'][i - 1]} for i in game['related']],
        'today': date.today(),
    }
    return render(request, 'pages/detail.html', context)


def context_demo(request, lang):
    t = TEXTS[lang]
    games_list = [{'title': name} for name in t['game_names']]
    context = {
        'title': t['ctx_title'],
        'games': games_list,
        'count': len(games_list),
        'user': request.user,
    }
    return render(request, 'pages/context.html', context)


def profile(request, lang):
    t = TEXTS[lang]
    context = {
        'username': t['username'],
        'balance': 1234.5,
        'joined': datetime.now(),
        'bio': t['bio'],
    }
    return render(request, 'pages/profile.html', context)


def games(request, lang):
    t = TEXTS[lang]
    category = request.GET.get('category', 'all')
    return HttpResponse(
        f"{t['category']}: {category}",
        content_type='text/plain; charset=utf-8',
    )


def old_games(request, lang):
    # Переадресация: старый адрес /casino/ теперь ведёт на /games/ (HTTP 302)
    return redirect(prefix(lang) + '/games/')
