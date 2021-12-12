
# Create your views here.
import csv
import io
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib import messages
from .models import Employee
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json

from django.http import JsonResponse


class GetAllProfiles(LoginRequiredMixin, APIView):

    template_name = 'all_profiles.html'
    login_url = '/login/'
    redirect_field_name = 'login'

    def get(self, request):
        lst = []
        mpdata = Employee.objects.all()
        for val in mpdata:
            dict = {}
            dict['EmpCode'] = val.EmpCode
            dict['EmpName'] = val.EmpName
            dict['Dept'] = val.Dept
            dict['Age'] = val.Age
            dict['Experience'] = val.Experience

            lst.append(dict)

        return render(request, 'all_profiles.html', {'Emp_details': lst})

    def post(self, request, *args, **kwargs):

        empcode = request.POST['empcode']

        del_employee = Employee.objects.get(EmpCode=empcode).delete()
        return render(request, 'all_profiles.html')


class UploadProfile(TemplateView, LoginRequiredMixin):
    permission_classes = (IsAuthenticated,)
    template_name = 'profile_upload.html'
    login_url = '/login/'
    redirect_field_name = 'login'

    def post(self, request, *args, **kwargs):

        empcode = request.POST['empcode']
        empname = request.POST['empname']
        age = request.POST['age']
        dept = request.POST['dept']
        experience = request.POST['experience']

        add_employee = Employee.objects.create(EmpCode=empcode, EmpName=empname,
                                               Age=age, Dept=dept, Experience=experience)

        return render(request, 'profile_upload.html')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def edit(request, empcode):
    print(empcode)
    content = Employee.objects.get(EmpCode=empcode)
    return render(request, 'profile_edit.html', {'datas': content})


def update(request, empcode):
    edit_data = Employee.objects.get(EmpCode=empcode)
    if request.method == 'POST':
        edit_data.EmpCode = request.POST.get('empcode')
        edit_data.EmpName = request.POST.get('empname')
        edit_data.Course = request.POST.get('dept')
        edit_data.Experience = request.POST.get('experience')
        edit_data.Age = request.POST.get('age')
        edit_data.save()
        return redirect('/get-all-profiles')


def login(request):
    return render(request, 'login.html')


def login_call(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        request.session.set_expiry(36000)  # 1 hour
        return redirect('/upload-profile')
    else:
        return redirect('/upload-profile')


def remove(request, empcode):
    dt = Employee.objects.filter(EmpCode=empcode)
    dt.delete()
    return redirect('/get-all-profiles')


def logout_view(request):
    logout(request)
    return redirect('/login')
