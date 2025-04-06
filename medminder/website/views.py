# views.py
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import IntroForm, MedicationNameForm, DosageForm, FrequencyForm

FORMS = [
    ("intro", IntroForm),
    ("medication_name", MedicationNameForm),
    ("dosage", DosageForm),
    ("frequency", FrequencyForm),
]

TEMPLATES = {
    "intro": "website/medication_wizard/wizard.html",
    "medication_name": "website/medication_wizard/wizard.html",
    "dosage": "website/medication_wizard/wizard.html",
    "frequency": "website/medication_wizard/wizard.html",
    "done": "website/medication_wizard/done.html",
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

def website(request):
    """
    Render the index page of the website.
    """
    print("Rendering index page")  # Debug
    return render(request, 'website/sidebar.html')