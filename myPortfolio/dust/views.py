# dust/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact form data to the database
            return render(request, 'dust/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'dust/contact.html', {'form': form})

def about(request):
    return render(request, 'dust/about.html')

def projects(request):
    return render(request, 'dust/projects.html')

def home(request):
    return render(request, 'dust/home.html')
