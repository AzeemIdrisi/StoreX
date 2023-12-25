# using django model form to replicate model into form without manually creating a form
from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
        ]
