from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag(name='time')
def curr_time(format_string='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(format_string)
