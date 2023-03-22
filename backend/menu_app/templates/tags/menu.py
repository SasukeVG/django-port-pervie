from django import template
from backend.menu_app.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu_app/menu.html')
def draw_menu(name):
    try:
        menu = Menu.objects.prefetch_related('menu_items').get(name=name)
    except Menu.DoesNotExist:
        menu = None
    return {'menu': menu}
