from django.db import models
from django.db.models import fields
from rest_framework import fields, serializers

from .models import Accept, Appointment

class MakeAnAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'request', 'sent_date')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accept
        fields = ('accepted', 'accepted_date')