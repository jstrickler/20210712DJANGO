import pdb

from django.shortcuts import render
from .forms import DogForm
import logging

logging.basicConfig(
    filename="dogs.log",
    level=logging.DEBUG,
)

# logging.critical()
# logging.warn(...)
# logging.error(...)
# logging.info()
# loging.debug()
import pdb

def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            pdb.set_trace()  # jump into the debugger.
            form.save()  # save to database
            logging.info(f"Saved new dog {form.cleaned_data.get('name')}")
            data = {
                'dog': form.cleaned_data
            }
            return render(request, 'dogs_core/dog_saved.html', data)
    else:
        form = DogForm()
        data = {
            'form': form
        }
        return render(request, 'dogs_core/add_dog.html', data)

