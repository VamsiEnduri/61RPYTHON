from django.urls import path
from .views import empform,create_emp
urlpatterns=[
    path("",empform),
    path("api/create_emp/",create_emp)
]

# 127.0.0.:8000/api/create_emp/