from django.urls import path
from .views import empForm,create_emp,get_emps,delete_emp,edit_emp
urlpatterns=[
    path("",empForm),
    path("api/create_emp/",create_emp),
    path("api/get_emps/",get_emps),
    path("api/delete_emp/<int:__id>",delete_emp),
    path("api/edit_emp/<int:__id>",edit_emp)
]