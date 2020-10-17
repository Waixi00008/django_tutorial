from django import template
register = template.Library()

@register.filter
def add_filter(value,args):
    return value+args