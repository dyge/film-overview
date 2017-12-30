from verwaltung.models import Film
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

def index(request):
    queryset_list = Film.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(Q(titel__icontains=query)|Q(genre__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {"object_list":queryset, "page": 'page',}
    return render(request, "index.html", context)
