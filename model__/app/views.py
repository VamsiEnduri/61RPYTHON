from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Emps
# Create your views here.

@api_view(["POST"])
def create_emp(request):
    print(request.data)
    reData=request.data
    Emps.objects.create(
        name=reData["name"],
        email=reData["email"],
        salary=reData["salary"],
    )
    return Response({"msg":"abc"})
    # insert into emps (name,email,salary) values (1,2,3)
    


def empForm(request):
    return render(request,"empform.html")
