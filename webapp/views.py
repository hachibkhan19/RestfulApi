from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializers
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Hachib khan'
        context['country'] = 'Bangladesh'
        context['list'] = [1, 2, 3, 4, 5]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializers(employees, many=True)
        return Response(serializer.data)

    def post(self):
        pass


