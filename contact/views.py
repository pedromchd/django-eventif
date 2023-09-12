from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        return handle(request)
    return new(request)

def new(request, form = ContactForm()):
    return render(request, 'contact/contact_form.html', { 'form': form })

def handle(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return new(request, form)

    _send_mail(
        subject = f'Nova mensagem de {form.cleaned_data.get("name")}',
        body = ('contact/contact_email.txt', form.cleaned_data),
        from_email = form.cleaned_data.get('email'),
        recipients = (settings.DEFAULT_FROM_EMAIL, form.cleaned_data.get('email'))
    )

    messages.success(request, 'Mensagem enviada com sucesso!')
    return HttpResponseRedirect('/contato/')

def _send_mail(subject, body, from_email, recipients):
    message = render_to_string(*body)
    mail.send_mail(subject, message, from_email, recipients)
