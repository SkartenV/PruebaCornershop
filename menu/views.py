from django.shortcuts import render
from .forms import MenuForm#, OpcionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Menu

def Add_Menu(request):
    form = MenuForm()

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MenuForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form})

def CantidadMenu(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_menu = Menu.objects.all().count()

    return render(
        request,
        'home.html',
        context={'num_menu':num_menu},
    )