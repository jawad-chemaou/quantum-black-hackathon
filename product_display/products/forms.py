from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput)  # Champ mot de passe masqué

    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'age', 'email', 'adresse', 'mot_de_passe']
