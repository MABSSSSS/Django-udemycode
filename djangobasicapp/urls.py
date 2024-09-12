
from django.urls import path 

from .import views



urlpatterns=[
path("", views.Index,name="Home"),
path("Index", views.Index,name="Index"),
path("Home", views.Home,name="Home"),
path("ShowMessages", views.ShowMessages,name="SM"),
path("UseVariable", views.UseVariable,name="UVR"),
path("GetRequestDemo", views.GetRequestDemo,name="GRV"),
path("ShowDateTimeInfo", views.ShowDateTimeInfo,name="SDTI"),
path("LoggingExample", views.LoggingExample,name="LoggingExample"),
path("iftagdemo", views.iftagdemo,name="IFTAGDEMO"),
path("ShowProducts", views.ShowProducts,name="SP"),
path("ShowUsers", views.LoadUsers,name="LU"),
path("ShowUsers2", views.LoadUsers2,name="LU2"),
path("ShowUsersDetails", views.LoadUserDetails, name="ShowUserDetails"),
path("PassModel", views.PassModelToTemplate, name="LoadUsers2"),

        
]


