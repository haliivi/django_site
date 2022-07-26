from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }
    # return HttpResponse('Страница приложения women.')
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu,
                                                'title': 'О сайте'})


# def categories(request, catid):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         # raise Http404()
#         return redirect('home', permanent=False)
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def add_page(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Обратня связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с {post_id=}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Странца не найдена</h1>')
