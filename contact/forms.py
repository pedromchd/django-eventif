from django import forms

from contact.models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Nome:')
    email = forms.EmailField(label='Email:', widget=forms.EmailInput)
    phone = forms.CharField(label='Telefone:', required=False, empty_value='Não informado')
    message = forms.CharField(label='Mensagem:', widget=forms.Textarea)
