from django.urls import path
from . import views
from .views import MedicationWizard

urlpatterns = [
    path('', views.website, name='website'),
    path('add-plan/', MedicationWizard.as_view(), name='medication_wizard'),
]
