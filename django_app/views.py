from django.shortcuts import render
from .models import *


def index(request) :
    categories = Category.objects.all ()
    news = News.objects.all ()
    return render ( request, 'index.html', {'categories' : categories, 'news' : news} )