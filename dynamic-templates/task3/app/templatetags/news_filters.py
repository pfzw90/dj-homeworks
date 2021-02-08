from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='format_date')
def format_date(d: float) -> str:
    diff = datetime.timestamp(datetime.now()) - d
    if diff < 600:
        return 'Только что'
    elif diff < (24 * 3600):
        return f'{int(diff // 3600)} часов назад'
    else:
        return datetime.utcfromtimestamp(d).strftime("%Y/%m/%d")


@register.filter(name='format_num_comments')
def format_num_comments(n: str) -> str:
    if int(n) == 0:
        return 'Оставьте комментарий'
    elif int(n) < 50:
        return n
    elif int(n) >= 50:
        return '50+'


@register.filter(name='format_score')
def format_score(n: str, default: str) -> str:
    if n:
        if int(n) < -5:
            return 'Все плохо!'
        elif -5 <= int(n) <= 5:
            return 'Нейтрально'
        elif int(n) > 5:
            return 'Хорошо'
    else:
        return default


@register.filter(name='format_selftext')
def format_selftext(text: str, count: int) -> str:
    split = text.split(' ')
    return ' '.join(split[:count - 1]) + ' . . . ' + ' '.join(split[-count:])
