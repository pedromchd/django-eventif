from django.shortcuts import render

from contact.forms import ContactForm

def contact(request):
    return render(request, 'contact/contact_form.html', { 'form': ContactForm() })
