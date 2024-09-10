import datetime
from django.http import HttpResponse
from django.shortcuts import render
import requests
import logging

# function based view
def Home(request):
    return HttpResponse("<h1>Hello World from Django 5.</h1>")


def ShowMessages(request):
    return HttpResponse("<h1>Hello World from Django 5.</h1><h2>Hello, now I am in heading 2</h2>")


def UseVariable(request):
    Message = "<h1>Welcome To Django Development</h1>" * 7
    return HttpResponse(Message)


def GetRequestDemo(request):
    # Handle GET requests with parameters
    Message = ''
    if request.method == 'GET':
        Message = request.GET.get('Message', "<h1>You want to supply values for the message parameter</h1>")
        Message += request.GET.get('Country', "<h1>You want to supply values for the country parameter</h1>")
    return HttpResponse(Message)


def ShowDateTimeInfo(request):
    TodaysDate = datetime.datetime.now()
    templatefilename = "djangobasicapp/Show.html"
    context = {'TodaysDate': TodaysDate}
    return render(request, templatefilename, context)


def LoggingExample(request):
    logging.basicConfig(level=logging.DEBUG)
    
    logging.debug(f"Debug: I just entered the view at {(datetime.datetime.now())}")   
    logging.info(f"Info: Confirmation that things are working as expected.")   
    logging.warning(f"Warning: An indication that something unexpected happened.")   
    logging.error(f"Error: Due to a more serious problem, the software has not been able to perform.")   
    logging.critical(f"Critical: A serious error, indicating that the program itself may be unable.")   
    
    custom_logger = logging.getLogger('mycustom_logger')
    custom_logger.debug(f"Debug: I just entered the view at {datetime.datetime.now()}")
    custom_logger.info("Info: Confirmation that things are working as expected.")
    custom_logger.warning("Warning: An indication that something unexpected happened.")
    custom_logger.error("Error: Due to a more serious problem, the software has not been able to perform.")
    custom_logger.critical("Critical: A serious error, indicating that the program itself may be unable.")
    
    return HttpResponse("Logging Demo")


def iftagdemo(request):
    data = {
        'name': 'James',
        'isVisible': True, 
        'loggedIn': False,
        'countrycode': 'Pakistan',
        'workExperience': 35,
        'stateCode': 'Hurrah'
    }
    templatefilename = "djangobasicapp/IfTagDemo.html"
    dict = {"Data": data}
    return render(request, templatefilename, dict)


def ShowProducts(request):
    Products = [
        {'ProductID': 1, 'ProductName': 'Laptop', 'Quantity': 10, 'UnitsInStock': 50, 'Discontinued': False, 'Cost': 1000.00},
        {'ProductID': 2, 'ProductName': 'Smartphone', 'Quantity': 25, 'UnitsInStock': 100, 'Discontinued': False, 'Cost': 500.00},
        {'ProductID': 3, 'ProductName': 'Tablet', 'Quantity': 15, 'UnitsInStock': 75, 'Discontinued': False, 'Cost': 300.00},
        {'ProductID': 4, 'ProductName': 'Monitor', 'Quantity': 20, 'UnitsInStock': 60, 'Discontinued': False, 'Cost': 150.00},
        {'ProductID': 5, 'ProductName': 'Keyboard', 'Quantity': 50, 'UnitsInStock': 200, 'Discontinued': False, 'Cost': 25.00},
        {'ProductID': 6, 'ProductName': 'Mouse', 'Quantity': 60, 'UnitsInStock': 250, 'Discontinued': False, 'Cost': 15.00},
        {'ProductID': 7, 'ProductName': 'Printer', 'Quantity': 5, 'UnitsInStock': 30, 'Discontinued': True, 'Cost': 200.00},
        {'ProductID': 8, 'ProductName': 'Headphones', 'Quantity': 40, 'UnitsInStock': 120, 'Discontinued': False, 'Cost': 75.00}
    ]
    
    Processors = [
        {'Category': 'AMD', 'processors': ['Ryzen 3990', 'Ryzen 3970', 'Ryzen 3960', 'Ryzen 3950']},
        {'Category': 'Intel', 'processors': ['Xeon 8362', 'Xeon 8358', 'Xeon 8380']}
    ]
    
    templatefile = 'djangobasicapp/ShowProducts.html'
    context = {"Products": Products, "TotalProducts": len(Products), "Processors": Processors}
    
    return render(request, templatefile, context)


def LoadUsers(request):
    templatefilename = "djangobasicapp/ShowUsers.html"
    response = CallRestAPI()
    if response.status_code == 200:
        users = response.json()
    else:
        users = []
    context = {"users": users}
    return render(request, templatefilename, context)


def CallRestAPI():
    BASE_URL = 'https://fakestoreapi.com'
    try:
        response = requests.get(f"{BASE_URL}/users")
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        logging.error(f"API call failed: {e}")
        return None
    return response


def Index(request):
    return render(request, 'djangobasicapp/Index.html')


def LoadUsers2(request):
    templatefilename = "djangobasicapp/ShowUsersasCards.html"
    image = 'https://i.pravatar.cc/150'
    response = CallRestAPI()
    if response:
        users = response.json()
    else:
        users = []
    context = {"users": users, "image": image}
    return render(request, templatefilename, context)
