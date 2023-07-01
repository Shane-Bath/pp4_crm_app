from django import forms
from .models import Client, PhoneLog
# from allauth.account.forms import SignupForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'middle_name', 'last_name',
                  'phone_number', 'email_address' , 'address', 'eircode')


class CallLogForm(forms.ModelForm):
    class Meta:
        model = PhoneLog
        fields = ('first_name', 'last_name', 'phone_number', 'message')

    # check_client = forms.ModelChoiceField(
    #     queryset=Client.objects.all(),
    #     to_field_name='first_name',
    #     required=True,
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
