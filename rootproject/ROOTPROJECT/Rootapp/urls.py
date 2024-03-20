from django.urls import path
from .views import *
urlpatterns=[
    path('hello/',hello),
    path('index/',index),
    path("dtl/",show_dtl),
    path("unknown/",unknow),
    path("calc/",calculator)
]