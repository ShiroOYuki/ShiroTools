from django import template

register = template.Library()

@register.filter
def toString(val):
    return str(val)