# your_app/templatetags/template_filters.py

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Custom filter to get a value from a dictionary by key."""
    return dictionary.get(key)
