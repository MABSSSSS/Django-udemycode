
from django.urls import path 

from .import views



urlpatterns=[
path("", views.Home,name="Home"),
path("Home", views.Home,name="Home"),
path("ShowMessages", views.ShowMessages,name="SM"),
path("UseVariables", views.UseVariable,name="UVR"),
path("GetRequestDemo", views.GetRequestDemo,name="GRV"),
path("ShowDateTimeInfo", views.ShowDateTimeInfo,name="SDTI"),
path("LoggingExample", views.LoggingExample,name="LoggingExample")

        
]


