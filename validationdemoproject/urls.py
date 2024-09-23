
from django.contrib import admin
from django.urls import path
from validationsdemoapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp, name="signup"),
]
