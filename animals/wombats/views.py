from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

def wombat_get(request, pk=None):
    if pk is not None:
        data = my_serializer(Wombat.objects.all())
        return data
    else:
        data = my_serializer(Wombat.objects.get(pk=pk))
        return data


# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Wombats are Fun!")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Wombats are Fun!" }
#     return render(request, 'wombats/home.html', context)
