from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from itsdangerous import Serializer

from .serializer import AppointmentSerializer, MakeAnAppointmentSerializer
from .models import Accept, Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

class HomeTemplateView(GenericAPIView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")


class AppointmentDetail(GenericAPIView):
    
    serializer_class = MakeAnAppointmentSerializer
    model = Appointment
    queryset=Appointment.objects.all()


    def post(self, request):
        serializer_class = MakeAnAppointmentSerializer(data=request.data)
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            
        )

        appointment.save()
        
        serializer = MakeAnAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        appointment=Appointment.objects.all()
        serializer = MakeAnAppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

        

class ManageAppointmentDetail(GenericAPIView):
    serializer_class = AppointmentSerializer
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        appointment= self.get_object(pk)
        serializer= MakeAnAppointmentSerializer(appointment)
        return Response(serializer.data)
    def post(self, request, pk):
        email = request.POST.get("email")
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        name = request.POST.get("name")
        email = request.POST.get("email")
        appointment= Appointment.objects.all()
        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body= 'The date of the appointmeent is set to {{date}}.',
            from_email=settings.EMAIL_HOST_USER,
            to=email
        )
        email.send()
        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of ")
        return HttpResponseRedirect(request.path)


     