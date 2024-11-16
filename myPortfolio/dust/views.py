from django.shortcuts import render

def contact(request):
    return render(request, 'dust/contact.html')

def about(request):
    return render(request, 'dust/about.html')

def projects(request):
    return render(request, 'dust/projects.html')
def home (request):
    return render(request, 'dust/home.html')