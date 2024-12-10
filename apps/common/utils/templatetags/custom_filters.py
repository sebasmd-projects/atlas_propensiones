from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def add_class(field, css_class):
    try:
        widget = field.as_widget(attrs={"class": css_class})
        return mark_safe(widget)
    except AttributeError:
        return field


@register.filter
def currency(value):
    try:
        value = float(value)
        return f"$ {value:,.2f}"
    except (ValueError, TypeError):
        return value
