from django.urls import path

from . import views
app_name = 'menu_app'
urlpatterns = [
    path('<int:selected_menu_item_id>/', views.menu, name='menu'),
    # path('', views.index, name='index'),
    path('', views.menu, name='menu'),
]