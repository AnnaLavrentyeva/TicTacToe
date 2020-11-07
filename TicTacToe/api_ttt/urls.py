from django.conf.urls import url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
   # url(r'^movement', views.movement),
   # url(r'', TemplateView.as_view(template_name ="index.html")),
    url(r'^game', views.game),
]
