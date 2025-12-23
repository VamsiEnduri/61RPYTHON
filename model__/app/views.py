from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Emps
# Create your views here.

@api_view(["PUT"])
def edit_emp(request,__id):
    reqData=request.data
    editableEmp=Emps.objects.get(id=__id)
    editableEmp.name=reqData["name"]
    editableEmp.email=reqData["email"]
    editableEmp.salary=reqData["salary"]
    editableEmp.save()

    return Response({"msg":f"{__id} emp edited successfully...."})

@api_view(["DELETE"])
def delete_emp(request,__id):
    Emps.objects.get(id=__id).delete() # delete from emps where id=2
    return Response({"msg":f"{__id} em is deleted successfully...."})

@api_view(["GET"])
def get_emps(request):
    emps=Emps.objects.values()
    return Response({"msg":"e,ps fetrched succesdfully","data":emps})
    # emps=list(Emps.objects.values())
    # return Response({"msg":"e,ps fetrched succesdfully","data":emps})
    

@api_view(["POST"]) #post drf
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
