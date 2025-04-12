from django.urls import path
from . import views
from .views import LandingPageView, MedicationWizard

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('add-plan/', MedicationWizard.as_view(), name='medication_wizard'),
]
