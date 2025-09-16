from django.shortcuts import render, redirect
from.forms import ContactForm
form .models import MenuItem
form django.core.mail import send_email
from django.conf import settings

def home(request):
    query = request.GET.get("q", "")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"New Contact Form Submisssion from {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"


            send_email(
                subject, full_message, settings.DEFAULT_FORM_EMAIL, [settings.EMAIL_HOST_USER],
                fail_silently = False,

            )
            
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "home.html",{
        "form": form,
        "menu_items": menu_items,
        "query": query
        })



