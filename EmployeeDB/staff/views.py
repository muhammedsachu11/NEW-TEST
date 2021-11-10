
# Create your views here.
import csv
import io
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


class UploadProfile(LoginRequiredMixin, TemplateView):
    permission_classes = (IsAuthenticated,)
    template_name = 'profile_upload.html'
    login_url = '/login/'
    redirect_field_name = 'login'

    def post(self, request):

        template = "profile_upload.html"
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        else:
            messages.error(request, 'Successfully entered the profiles')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = Employee.objects.update_or_create(
                EmpCode=column[0],
                EmpName=column[1],
                Dept=column[2],
                Age=column[3],
                Experience=column[4]
            )
        context = {}
        return render(request, template, context)


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def login_call(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        request.session.set_expiry(36000)  # 1 hour
        return redirect('/upload-csv')
    else:
        return redirect('/upload-csv')


def logout_view(request):
    logout(request)
    return redirect('/login')
