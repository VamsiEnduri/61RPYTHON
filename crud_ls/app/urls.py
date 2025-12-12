from django.urls import path
from .views import empform,create_emp,delete_emp,edit_emp
urlpatterns=[
    path("",empform),
    path("api/create_emp/",create_emp),
    path("api/delete_emp/<int:id>/",delete_emp),
    path("api/edit_emp/<int:id>/",edit_emp)
]

# 127.0.0.:8000/api/create_emp/