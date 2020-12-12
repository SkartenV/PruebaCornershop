from django.shortcuts import render
from .forms import MenuForm#, OpcionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Menu
from django.views import generic

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

class MenuListView(generic.ListView):
    model = Menu

def Edit_Menu(request, menu_id):
    instancia = Menu.objects.get(id=menu_id)
    form = MenuForm(instance=instancia)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return HttpResponseRedirect('list/')
    return render(request, "edit_menu.html", {'form': form})

def CantidadMenu(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_menu = Menu.objects.all().count()
    return render(request, "home.html", {'num_menu': num_menu})