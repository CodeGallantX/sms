from django import template
from django.contrib.messages import get_messages

register = template.Library()

@register.inclusion_tag('templatetags/toasts.html', takes_context=True)
def toasts(context):
    messages = get_messages(context['request'])
    return {'messages': messages}
