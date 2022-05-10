from django.urls import path
from .views import AppointmentDetail, ManageAppointmentDetail

urlpatterns = [
    path("api/make-an-appointment/", AppointmentDetail.as_view(), name="appointment"),
    path('api/manage-appointment/<int:pk>/', ManageAppointmentDetail.as_view(), name="manage"),
    ]
