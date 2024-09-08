
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("djangobasicapp/", include("djangobasicapp.urls")),
    path("djangobasicapp2/", include("djangobasicapp2.urls")),
    path("djangobasicapp3/", include("djangobasicapp3.urls")),

]
