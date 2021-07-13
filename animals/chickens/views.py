from django.http import HttpResponse, Http404  # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.



# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Chickens!")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Chickens!" }
#     return render(request, 'chickens/home.html', context)
def home(request):
    return HttpResponse("Welcome to Chickens!")

def cluck(request):
    context = {
        'color': 'green',
        'value': 5.683,
    }
    return render(request, 'chickens/cluck.html', context)

def greet(request, color):
    return HttpResponse(f"You selected {color}")

def repeat(request, count):
    text = 'WOW!' * count
    return HttpResponse(text)

def fail(request):
    #  s = get_object_or_404(....)
    raise Http404("All is terrible")

#  https://localhost/chickens/1
#  https://localhost/chickens/2
#  'chickens/<int:pk>'

def get_record(request, pk):
    return HttpResponse(f"You want record #{pk}")