from django import template

from home_page.models import *

register = template.Library()

@register.simple_tag()
def get_high_ranking_teachers():
    return Teacher.objects.all().filter(rating__gte=8)

@register.simple_tag()
def get_teachers(sort=None, gte=None):
    list = Teacher.objects.all()
    if sort:
        list = list.order_by(sort)
    if not gte:
        return list
    else:
        return list.filter(rating__gte=gte)

@register.inclusion_tag('home_page/temp.html')
def show_teachers(sort=None, gte=0):
    teachers_list = get_teachers(sort=sort, gte=gte)
    return {"list": teachers_list}