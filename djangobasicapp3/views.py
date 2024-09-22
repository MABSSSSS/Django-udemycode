from django.shortcuts import render

# Create your views here.

def Home(request):
    templatefilename="djangobasicsapp3/Home.html"
    return render(request,templatefilename)