from .translations import DEFAULT_LANG, LANG_LABELS, LANGUAGES, TEXTS


def i18n(request):
    """Даёт каждому шаблону тексты `t`, код языка, префикс ссылок и переключатель языков."""
    match = request.resolver_match
    lang = (match.kwargs.get('lang') if match else None) or DEFAULT_LANG
    if lang not in TEXTS:
        lang = DEFAULT_LANG

    prefix = '' if lang == DEFAULT_LANG else f'/{lang}'
    rest = request.path[len(prefix):] or '/'
    query = request.META.get('QUERY_STRING', '')
    suffix = f'?{query}' if query else ''

    return {
        't': TEXTS[lang],
        'lang': lang,
        'lp': prefix,
        'languages': [
            {'code': code, 'label': LANG_LABELS[code],
             'url': ('' if code == DEFAULT_LANG else f'/{code}') + rest + suffix}
            for code in LANGUAGES
        ],
    }
