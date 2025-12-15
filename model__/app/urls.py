from django.urls import path
from .views import empForm,create_emp
urlpatterns=[
    path("",empForm),
    path("api/create_emp/",create_emp)
]