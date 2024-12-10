# pip install markdown

import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text, only_one_param):
    print('You can add to custom filters!', only_one_param)
    return mark_safe(markdown.markdown(text))
