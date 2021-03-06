from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import Http404, get_object_or_404, render
from .models import Superhero

# Note: automagic 404 does not work when DEBUG=True

def hero404(request, hero_name):
    try:
        hero = Superhero.objects.get(name=hero_name)
    except:
        raise Http404("Hero '{}' not found [{}]".format(
                hero_name,
                request.get_full_path(),
            )
        )
    response = HttpResponse('<h1>Info for {} ({})</h1>'.format(
        hero_name,
        hero.secret_identity,
        )
    )
    return response


def hero404sc(request, hero_name):

    hero =  get_object_or_404(Superhero, name=hero_name)

    return HttpResponse('<h1>Info for {} ({})</h1>'.format(
            hero_name,
            hero.secret_identity,
        )
    )

def handler404(request, *args, **argv):
    response = render('superheroes/404.html', {},
                                 context_instance=RequestContext(request))
    response.status_code = 404
    return response