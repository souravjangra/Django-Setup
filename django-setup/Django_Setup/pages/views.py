from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "we are in about page",
        "my_number": 123,
        "my_list": [12,21,34,45,52, "Abc"],
        "my_title": '<h1>Hello World</h1>'
    }
    return render(request, "about.html", my_context)