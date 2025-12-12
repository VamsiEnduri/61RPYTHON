from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(["PUT"])
def edit_emp(request,id):
    return Response({"msg":f"you have edited {id} id item"})



@api_view(["DELETE"])
def delete_emp(request,id):
    return Response({"msg":f"you have deleted {id} id item"})

def empform(request):
    return render(request,"emp.html")

@api_view(["POST"])
def create_emp(request):
    emps=request.data
    print(emps)
    return Response({"msg":"emp created successfully","data":emps})