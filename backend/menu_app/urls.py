from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:selected_menu_item_id>/', views.index, name='index'),
    path('', views.index, name='index')
]