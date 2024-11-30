from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.character_list, name="list"),
    path('new-character/', views.new_character, name="new-character"),
    path('<slug:slug>', views.character_page, name='character'),
]