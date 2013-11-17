from django import template
register = template.Library()

@register.filter
def contains(url, value):
    return value in url
