from django import template

register = template.Library()


@register.inclusion_tag('pagination.html')
def pagination(total, current_num):
    return {'total': range(1, total + 1), 'current_num': current_num}

