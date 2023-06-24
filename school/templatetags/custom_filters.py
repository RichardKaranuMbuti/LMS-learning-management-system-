from django import template

register = template.Library()

@register.filter
def add_css_classes(field, css_classes):
    classes = field.field.widget.attrs.get('class', '')
    classes += f' {css_classes}'
    field.field.widget.attrs['class'] = classes
    return field
