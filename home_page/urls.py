from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#app_name = "home_page"
from .views import *

urlpatterns = [
    # ex: /
    path('', views.home_page_view, name='home'),

    # ex: /teachers
    path("teachers", show_teachers.as_view(), name='teachers',),
    # ex: /add_teacher
    path("add_teacher", views.add_teacher, name='add_teacher',),
    # ex: /teachers/anastasia_linenko
    path("teacher/<slug:teacher_slug>", views.show_teacher, name='teacher'),

    # ex: /account
    path("account", views.account, name='account'),
    # ex: /translation
    path("translation", views.translation, name='translation'),
    # ex: /curces
    path("curces", views.curces, name='curces'),
    # ex: /about_us
    path("about_us", views.about_us, name='about_us'),
    # ex: /login
    path("login", views.login, name='login'),
    # ex: /registration
    path("registration", views.registration, name='registration'),


    # ex: /temp_fun
#    path("temp_fun", views.temp_fun, name='temp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)