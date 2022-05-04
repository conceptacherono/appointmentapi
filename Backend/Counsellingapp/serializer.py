from django.db import models
from django.db.models import fields
from rest_framework import fields, serializers

from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'request', 'sent_date', 'accepted', 'accepted_date')