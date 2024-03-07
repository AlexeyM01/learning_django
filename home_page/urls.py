from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = "home_page"
from .views import *

urlpatterns = [
    # ex: /
    path('', HomePageView.as_view(), name='home'),

    # ex: /teachers
    path("teachers", ShowAllTeachers.as_view(), name='teachers'),
    # ex: /add_teacher
    path("add_teacher", AddTeacher.as_view(), name='add_teacher'),
    # ex: /teachers/anastasia_linenko
    path("teacher/<slug:teacher_slug>", ShowTeacher.as_view(), name='teacher'),


    # ex: /login
    path("login", LoginUser.as_view(), name='login'),
    # ex: /logout
    path("logout", logout_user, name='logout'),
    # ex: /registration
    path("registration", UserRegistration.as_view(), name='registration'),

    # ex: /translation
    path("translation", views.translation, name='translation'),
    # ex: /curses
    path("curses", views.curses, name='curses'),
    # ex: /about_us
    path("about_us", views.about_us, name='about_us'),

                  # ex: /temp_fun
    # path("temp_fun", views.temp_fun, name='temp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
