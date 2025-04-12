# views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings # To get LOGIN_REDIRECT_URL
from formtools.wizard.views import SessionWizardView
from .forms import IntroForm, MedicationNameForm, DosageForm, FrequencyForm

FORMS = [
    ("intro", IntroForm),
    ("medication_name", MedicationNameForm),
    ("dosage", DosageForm),
    ("frequency", FrequencyForm),
]

TEMPLATES = {
    "intro": "core/medication_wizard/wizard.html",
    "medication_name": "core/medication_wizard/wizard.html",
    "dosage": "core/medication_wizard/wizard.html",
    "frequency": "core/medication_wizard/wizard.html",
    "done": "core/medication_wizard/done.html",
}

class MedicationWizard(SessionWizardView):
    template_name = "medication_wizard/wizard.html"
    form_list = FORMS  # Ensure this line is present and correct

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        all_data = {}
        for form in form_list:
            all_data.update(form.cleaned_data)

        return render(self.request, 'medication_wizard/done.html', {'all_data': all_data})

def core(request):
    """
    Render the index page of the core.
    """
    print("Rendering index page")  # Debug
    return render(request, 'core/sidebar.html')

class LandingPageView(TemplateView):
    template_name = "core/landing_page.html"

    def get(self, request, *args, **kwargs):
        # If the user is already authenticated, redirect them away from the landing page
        if request.user.is_authenticated:
            # Redirect to the URL specified in settings.LOGIN_REDIRECT_URL
            # Or directly to a known dashboard url name if preferred:
            # return redirect(reverse('reminders:dashboard')) # Adjust accounts/url name if needed
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().get(request, *args, **kwargs)