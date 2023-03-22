from typing import List

from django.shortcuts import render
from .models import Menu, MenuItem


def index(request):
    # Define the context dictionary

    #menu: Menu = Menu(name='Main Menu')
    menu = Menu.objects.first()
    context = {'menu': menu}
    #print(menu.__dict__)
    #titles: List[str] = ['Keyboards', 'Headphones', 'Mouses']
    #sub_tiles = ['Razer', 'Sony', 'StealSeries']

    #base_tiles = [MenuItem(title=title, url=title, named_url=title, menu=menu).save() for title in titles]
    #sub_tiles =  [MenuItem(title=title, url=title, named_url=title, menu=menu, parent=bt).save() for title in titles
    #                                                                for bt in base_tiles]
    # Render the template with the context dictionary
    return render(request, 'menu.html', context)