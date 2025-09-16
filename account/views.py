from django.shortcuts import render, redirect
from.forms import ContactForm
form .models import MenuItem

def home(request):
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "home.html",{
        "form": form,
        "menu_items": menu_items,
        "query": query
        })



