from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *
from .models import *

main_menu = [
    {'title': 'KOREANA', 'url_name': 'home'},
    {'title': 'Преподаватели', 'url_name': 'teachers'},
    {'title': 'Перевод', 'url_name': 'translation'},
    {'title': 'Курсы', 'url_name': 'curses'},
    #    {'title': 'Отзывы', 'url_name': ''},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Добавить преподавателя', 'url_name': 'add_teacher'}
]


class show_teachers(ListView):
    """Класс страницы показа всех преподавателей на базе шаблона teachers.html"""
    teachers_list = Teacher.objects.all()
    model = Teacher
    template_name = 'home_page/teachers.html'
    extra_context = {
        'teachers_list': teachers_list,
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        """Функция добавления дополнительных контексных данных"""
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'СТРАНИЦА О ПРЕПОДАХ'
        context['sort'] = self.request.GET.get('sort')
        return context

    def get_queryset(self):
        """Функция возврата списка преподавателей"""
        return Teacher


def home_page_view(request):
    """Функция отображения главной страницы с помощью шаблона homepage.html"""
    context = {
        'main_menu': main_menu,
        'title': 'Главная страница'
    }
    return render(request, 'home_page/homepage.html', context=context)


def temp_fun(request):
    """Функция-затычка, которая просто отображает побочную страницу"""
    return render(request, 'home_page/somepage.html', {'title': 'Побочная страница'})


def show_teacher(request, teacher_slug):
    """Функция отображения отдельного преподавателя на базе шаблона teacher_page.html"""
    teacher_info = get_object_or_404(Teacher, slug=teacher_slug)
    context = {
        'info': teacher_info,
        'main_menu': main_menu,
        'title': 'ПЕРСОНАЛЬНАЯ СТРАНИЦА ПРЕПОДАВАТЕЛЯ',
    }
    return render(request, 'home_page/teacher_page.html', context=context)


def add_teacher(request):
    """Функция добавления преподавателя в БД на базе формы AddTeacherForm и шаблона add_teacher.html"""
    if request.method == 'POST':
        form = AddTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddTeacherForm()
    context = {
        'form': form,
        'main_menu': main_menu,
        'title': 'Страница добавления учителя'
    }
    return render(request, 'home_page/add_teacher.html', context=context)


def account(request):
    """Функция-затычка, которая просто отображает страницу входа"""
    return HttpResponse('Здесь будет вход')


def translation(request):
    """Функция-затычка, которая просто отображает страницу переводов"""
    return HttpResponse('Здесь будет перевод')


def curses(request):
    """Функция-затычка, которая просто отображает страницу курсов"""
    return HttpResponse('Здесь будет список курсов')


def about_us(request):
    """Функция-затычка, которая просто отображает страницу "о нас" """
    return HttpResponse('Здесь будет информация о нас')


def login(request):
    """Функция-затычка, которая просто отображает страницу входа"""
    return HttpResponse('Здесь будет окно входа в аккаунт')


def registration(request):
    """Функция-затычка, которая просто отображает страницу регистрации"""
    return HttpResponse('Здесь будет окно регистрации')
