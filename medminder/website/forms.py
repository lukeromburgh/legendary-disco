# forms.py
from django import forms

class IntroForm(forms.Form):
    intro_message = forms.CharField(widget=forms.HiddenInput(), initial="Let's get you set up!")

class MedicationNameForm(forms.Form):
    medication_name = forms.CharField(label="What's the name of your medication?")

class DosageForm(forms.Form):
    dosage = forms.CharField(label="What dosage are you taking?")

class FrequencyForm(forms.Form):
    frequency = forms.ChoiceField(
        label="When would you like to be reminded?",
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
        ]
    )
    time = forms.TimeField(label="At what time?")
    until = forms.DateField(label="Until (dd/mm/yyyy)")