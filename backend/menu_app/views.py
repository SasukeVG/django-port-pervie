from typing import List, Optional

from django.shortcuts import render
from .models import Menu, MenuItem


def index(request, selected_menu_item_id: Optional[int] = None):
    menu = Menu.objects.get(name='Main Menu')
    print(selected_menu_item_id)
    context = {'menu': menu, 'selected_menu_item_id': selected_menu_item_id}
    return render(request, 'menu.html', context)