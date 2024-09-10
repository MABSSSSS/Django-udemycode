import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

import requests
# Create your views here.

# function based view
def Home(request):
    return HttpResponse("<h1>Hello World from Django 5.</h1>")


def ShowMessages(request):
    return HttpResponse("<h1>Hello World from Django 5.</h1><h2>Hello now I am in heading 2</h2>")


def UseVariable(request):
    Message = "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"
    Message += "<h1>Welcome To Django Development</h1>"

    return HttpResponse(Message)


def GetRequestDemo(request):
    #GET,PUT,POST,DELETE,PATCH
    Message=''
    if (request.method =='GET'):
       if (request.GET.get('Message')):
           Message = request.GET.get('Message')
       else:
           Message ="<h1>You want to  supplied values for messsage parameter</h1>"
           
         
    
       if (request.GET.get('Country')):
           Message += request.GET.get('Country')
       else:
           Message +="<h1>You want to  supplied values for country parameter</h1>"
           
    return HttpResponse(Message)
       
    
def ShowDateTimeInfo(request):
    TodaysDate = datetime.now()
    templatefilename = "djangobasicapp/Show.html"
    context = {'TodaysDate': TodaysDate}
    return render(request, templatefilename, context)

import logging
from datetime import datetime 

def LoggingExample(request):
    logging.debug(f"Debug : I just entered into View..{(datetime.now())}")   
    logging.info(f"Info : Confirmation that things are working as expected.")   
    logging.warning(f"Warning : An indication that something unexpected happened")   
    logging.error(f"Error :Due to more serious problem, the software has not been able to perform  ")   
    logging.critical(f"Critical : A serious error, indicating that the program itself may be unable")   
    
    custom_logger = logging.getLogger('mycustom_logger ')
    custom_logger.debug(f"Debug : I just entered into the View .. {datetime.now()}")
    custom_logger.info(f"Info: Confimation that things are working as expected.")
    custom_logger.warning(f"Warning : An indication that something unexpected happened.")
    custom_logger.error(f"Error: Due to more serious problem, the software has not been able to  .")
    custom_logger.critical(f"Critical: A serious error, indicating that the program itself may be.")

    
    return HttpResponse("Logging Demo")
    

def iftagdemo(request):
    data = {'name':'James ','isVisible':True, 'loggedIn': False , 'countrycode':'Pakistan', 'workExpereince':35, 'sateCode':'Hurrah'}
    templatefilename = "djangobasicapp/IfTagDemo.html"
    dict = {"Data": data}
    return render(request,templatefilename,dict) 
    
def ShowProducts(request):
    Products = []
    Processors = [
        {'Category':'AMD', 'processors':['Ryzen 3990', 'Ryzen 3970', 'Ryzen 3960', 'Ryzen 3950 ']},
        {'Category':'Intel', 'processors':['Xeon 8362' , 'Xeon 8358', 'Xeon 8380']}
    ];
    # Adding products using append method
    Products.append({
        'ProductID': 1,
        'ProductName': 'Laptop',
        'Quantity': 10,
        'UnitsInStock': 50,
        'Discontinued': False,
        'Cost': 1000.00
    })
    Products.append({
        'ProductID': 2,
        'ProductName': 'Smartphone',
        'Quantity': 25,
        'UnitsInStock': 100,
        'Discontinued': False,
        'Cost': 500.00
    })
    Products.append({
        'ProductID': 3,
        'ProductName': 'Tablet',
        'Quantity': 15,
        'UnitsInStock': 75,
        'Discontinued': False,
        'Cost': 300.00
    })
    Products.append({
        'ProductID': 4,
        'ProductName': 'Monitor',
        'Quantity': 20,
        'UnitsInStock': 60,
        'Discontinued': False,
        'Cost': 150.00
    })
    Products.append({
        'ProductID': 5,
        'ProductName': 'Keyboard',
        'Quantity': 50,
        'UnitsInStock': 200,
        'Discontinued': False,
        'Cost': 25.00
    })
    Products.append({
        'ProductID': 6,
        'ProductName': 'Mouse',
        'Quantity': 60,
        'UnitsInStock': 250,
        'Discontinued': False,
        'Cost': 15.00
    })
    Products.append({
        'ProductID': 7,
        'ProductName': 'Printer',
        'Quantity': 5,
        'UnitsInStock': 30,
        'Discontinued': True,
        'Cost': 200.00
    })
    Products.append({
        'ProductID': 8,
        'ProductName': 'Headphones',
        'Quantity': 40,
        'UnitsInStock': 120,
        'Discontinued': False,
        'Cost': 75.00
    })
    TemplateFile = 'djangobasicapp/ShowProducts.html'
    dict = {"Products": Products,"TotalProducts":len(Products),"Processors":Processors}
    
    return render (request,TemplateFile,dict)


def LoadUsers(request):
    templatefilename="djangobasicapp/ShowUsers.html"
    response = CallRestAPI()
    dict={"users":response.json()}
    return render(request, templatefilename,dict)
    
def CallRestAPI():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f"{BASE_URL}/users")
    return (response)  


def LoadUsers2(request):
    templatefilename="djangobasicapp/ShowUsersasCards.html"
    image = 'https://i.pravatar.cc';
    response = CallRestAPI()
    dict={"users":response.json(),"image":image}
    return render(request, templatefilename,dict)
    

    

    