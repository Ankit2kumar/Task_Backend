from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('general/',general_details),
    path('addsub/',csrf_exempt(add_subproduct)),
    path('savedetails/',csrf_exempt(save_details))
]
