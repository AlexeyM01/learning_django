from django import template

from home_page.models import *

register = template.Library()


@register.simple_tag()
def get_high_ranking_teachers():
    """Возвращает список преподавателей, персональный рейтинг который выше или равен 8"""
    return Teacher.objects.all().filter(rating__gte=8)


@register.simple_tag()
def get_teachers(sort=None, gte=None):
    """Возвращает список преподавателей с полученными параметрами типа сортировки и персональным рейтингом"""
    all_teachers_list = Teacher.objects.all()
    if sort:
        all_teachers_list = all_teachers_list.order_by(sort)
    if not gte:
        return all_teachers_list
    else:
        return all_teachers_list.filter(rating__gte=gte)


@register.inclusion_tag('home_page/temp.html')
def show_teachers(sort=None, gte=0):
    """Возвращает список преподавателей с выбранным типом сортировки и персональным рейтингом"""
    teachers_list = get_teachers(sort=sort, gte=gte)
    return {"list": teachers_list}
