from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views
from api_ttt.views import game_create_view_x, game_create_view_o
from django.views.generic import TemplateView

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^home/', views.home),
    path('create-game-x', game_create_view_x),
    path('create-game-o', game_create_view_o),
   # url(r'^movement', views.movement),
   # url(r'', TemplateView.as_view(template_name ="index.html")),
    url(r'^game_o', views.game_o),
    url(r'^game_x', views.game_x),
]
