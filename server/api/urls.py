from django.urls import path
from .views import VehicleUploadView

urlpatterns = [
    path('upload/', VehicleUploadView.as_view(), name='vehicle-upload'),
]
from django.urls import path
from .views import VehicleUploadView

urlpatterns = [
    path('upload/', VehicleUploadView.as_view(), name='vehicle-upload'),
]
