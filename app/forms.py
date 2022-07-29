from django import forms
from . import models
class CadastroForm(forms.ModelForm):
    class Meta:
        model = models.Cadastro
        fields = ['produto']