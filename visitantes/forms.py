from django import forms
from visitantes.models import Visitante

class visitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__"