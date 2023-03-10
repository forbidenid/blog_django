from django.shortcuts import render

# Create your views here.

def home_screen_view(request):

    context = {}
    context['some_string'] = "this is string that am passing to the view"


    return render(request, "personal/home.html", {})
    