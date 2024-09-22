from django.shortcuts import render

# Create your views here.


def Home(request):
    templatefilename ='djangobasicsapp2/home.html'
    
    return render(request, templatefilename)