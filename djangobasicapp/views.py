import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
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
    
    
    
    