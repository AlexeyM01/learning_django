from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *
from .models import *

main_menu = [
    {'title': 'KOREANA', 'url_name': 'home'},
    {'title': 'Преподаватели', 'url_name': 'teachers'},
    {'title': 'Перевод', 'url_name': 'translation'},
    {'title': 'Курсы', 'url_name': 'curces'},
    #    {'title': 'Отзывы', 'url_name': ''},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Добавить преподавателя', 'url_name': 'add_teacher'}
]

class show_teachers(ListView):
    teachers_list = Teacher.objects.all()
    model = Teacher
    template_name = 'home_page/teachers.html'
    extra_context = {
        'teachers_list': teachers_list,
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = main_menu
        context['title'] = 'СТРАНИЦА О ПРЕПОДАХ'
        context['sort'] = self.request.GET.get('sort')
        return context

    def get_queryset(self):
        return Teacher

def home_page_view(request):
    context = {
        'main_menu': main_menu,
        'title': 'Главная страница'
    }
    return render(request, 'home_page/homepage.html', context=context)


def temp_fun(request):
    return render(request, 'home_page/somepage.html', {'title': 'Побочная страница'})


def show_teacher(request, teacher_slug):
    teacher_info = get_object_or_404(Teacher, slug=teacher_slug)
    context = {
        'info': teacher_info,
        'main_menu': main_menu,
        'title': 'ПЕРСОНАЛЬНАЯ СТРАНИЦА ПРЕПОДАВАТЕЛЯ',
    }
    return render(request, 'home_page/teacher_page.html', context=context)


def add_teacher(request):
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
    return HttpResponse('Здесь будет вход')


def translation(request):
    return HttpResponse('Здесь будет перевод')


def curces(request):
    return HttpResponse('Здесь будет список курсов')


def about_us(request):
    return HttpResponse('Здесь будет информация о нас')


def login(request):
    return HttpResponse('Здесь будет окно входа в аккаунт')


def registration(request):
    return HttpResponse('Здесь будет окно регистрации')
