from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employee
from .serializers import EmployeeSerializer
import gspread
import requests
import io
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'index.jinja')

@api_view(['GET'])
def getSheetData(request):
    gc=gspread.service_account()
    sheet=gc.open_by_key("13yyd8s008LlRn0tn6LC5moH1fcBELBkYw2THX6gjdHU")
    worksheet=sheet.worksheet("Sheet1")
    values=worksheet.get_all_records()
    for i in range(0,len(values)):
        values[i]['firstName']=values[i].pop('First Name')
        values[i]['lastName']=values[i].pop('Last Name')
        values[i]['employeeID']=values[i].pop('Employee ID')
        values[i]['city']=values[i].pop('City')
    serializer=EmployeeSerializer(values,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def postSheetData(request):
    data=requests.get('http://127.0.0.1:8000/sheet/data')
    sheetData=data.json()
    for i in range(0,len(sheetData)):
        emp=employee()
        emp.firstName=sheetData[i]['firstName']
        emp.lastName=sheetData[i]['lastName']
        emp.employeeID=sheetData[i]['employeeID']
        emp.city=sheetData[i]['city']
        print("Sheets Data to Database")
        emp.save()
    return Response("You have successfully Fetched Data from Database and saved it in the Database")
        
        

@api_view(['GET','POST'])
def addemp(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            return render(request,'employeeform.jinja')
        elif request.method=="POST":
            firstName=request.POST['firstName']
            lastName=request.POST['lastName']
            city=request.POST['city']
            emp=employee(firstName=firstName,lastName=lastName,city=city)
            print('going to save in database')
            emp.save()
            messages.info(request,'Employee Successfully Added to Database')
            return redirect('/')
    else:
        messages.info(request,'Please login to Continue')
        return redirect('/auth/login')


@api_view(['GET'])
def emps(request):
    if request.user.is_authenticated:
        all_employees=employee.objects.all()
        return render(request,'employees.jinja',{'emps': all_employees })
    else:
        messages.info(request,'Please login to View Emplyees Data')
        return redirect('/auth/login')