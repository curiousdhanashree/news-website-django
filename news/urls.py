from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('technews', views.tech),
    path('business', views.business),
    path('entertainment', views.entertainment),
    path('health', views.health),
    path('science', views.science),
    path('about_us', views.about_us),
]
