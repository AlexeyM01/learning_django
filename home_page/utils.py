from .models import *

main_menu = [
    {'title': 'KOREANA', 'url_name': 'home'},
    {'title': 'Преподаватели', 'url_name': 'teachers'},
    {'title': 'Перевод', 'url_name': 'translation'},
    {'title': 'Курсы', 'url_name': 'curses'},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Добавить преподавателя', 'url_name': 'add_teacher'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['main_menu'] = main_menu
        return context
