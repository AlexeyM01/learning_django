from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from .models import *
from .utils import *

class ShowAllTeachers(DataMixin, ListView):
    """Класс страницы показа всех преподавателей на базе шаблона teachers.html"""
    model = Teacher
    paginate_by = 3
    template_name = 'home_page/teachers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Преподаватели")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        """Функция возврата списка преподавателей"""
        return Teacher.objects.all()

class HomePageView(DataMixin, ListView):
    template_name = 'home_page/homepage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="KOREANA")
        return dict(list(context.items()) + list(c_def.items()))

    @staticmethod
    def get_queryset():
        """Функция возврата списка преподавателей"""
        return Teacher


def temp_fun(request):
    """Функция-затычка, которая просто отображает побочную страницу"""
    return render(request, 'home_page/somepage.html', {'title': 'Побочная страница'})


class ShowTeacher(DataMixin, DetailView):
    model = Teacher
    template_name = 'home_page/teacher_page.html'
    slug_url_kwarg = 'teacher_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Страница преподавателя')
        return dict(list(context.items()) + list(c_def.items()))

class AddTeacher(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTeacherForm
    template_name = 'home_page/add_teacher.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление преподавателя")
        return dict(list(context.items()) + list(c_def.items()))



def translation(request):
    """Функция-затычка, которая просто отображает страницу переводов"""
    return HttpResponse('Здесь будет перевод')


def curses(request):
    """Функция-затычка, которая просто отображает страницу курсов"""
    return HttpResponse('Здесь будет список курсов')


def about_us(request):
    """Функция-затычка, которая просто отображает страницу "о нас" """
    return HttpResponse('Здесь будет информация о нас')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'home_page/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



class UserRegistration(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'home_page/user_registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

def logout_user(request):
    logout(request)
    return redirect('login')
