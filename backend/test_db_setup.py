from typing import List

from menu_app.models import Menu, MenuItem

menu: Menu = Menu(name='Main Menu').save()

titles: List[str] = ['Keyboards', 'Headphones', 'Mouses']
sub_tiles = ['Razer', 'Sony', 'StealSeries']

base_titles = [MenuItem(title=title, url=title, named_url=title, menu=menu).save() for title in titles]
sub_tiles =  [MenuItem(title=title, url=title, named_url=title, menu=menu, parent=bt).save() for title in sub_tiles for bt in base_titles]
