from django.urls import path

from .views import main_page, about_page

app_name = 'main'

urlpatterns = [
    path('', main_page, name='index'),
    path('about-me', about_page, name='about-me'),
]
