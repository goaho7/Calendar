from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def addid(field, css):
    return field.as_widget(attrs={'id': css})


@register.filter
def addname(field, css):
    return field.as_widget(attrs={'name': css})
