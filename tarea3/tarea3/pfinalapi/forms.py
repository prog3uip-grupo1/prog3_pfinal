from tarea3.pfinalapi.models import UserProfile
from tarea3.pfinalapi.serializers import UserProfileSerializer
from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')
    carnet = forms.CharField(max_length=10, label='Carnet')

    def signup(self, request, user):
        profile = UserProfile()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        user.profile = profile
        profile.user = user
        profile.carnet = self.cleaned_data['carnet']
        profile.save()

