from typing import List, Optional

from django.shortcuts import render
from .models import Menu, MenuItem

#
# def index(request, selected_menu_item_id: Optional[int] = None):
#     menu = Menu.objects.get(name='Main Menu')
#     print(selected_menu_item_id)
#     context = {'menu': menu, 'selected_menu_item_id': selected_menu_item_id}
#     return render(request, 'menu.html', context)


from django.shortcuts import render
from .models import MenuItem

def menu(request, selected_menu_item_id: Optional[int] = None):
    items = MenuItem.objects.all()
    top_level_items = []
    for item in items:
        if item.parent is None:
            top_level_items.append(item)

    context = {'top_level_items': top_level_items, 'selected_menu_item_id': selected_menu_item_id}
    return render(request, 'menu.html', context)

def get_sub_menu(item):
    sub_menu = []
    for child in item.children.all():
        sub_menu_item = {
            'name': child.name,
            'url': child.url,
        }
        if child.children.exists():
            sub_menu_item['children'] = get_sub_menu(child)
        sub_menu.append(sub_menu_item)
    return sub_menu
