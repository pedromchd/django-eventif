from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        return create(request)
    return new(request)


def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return new(request, form)

    cont = form.save()

    _send_email(
        subject='Nova mensagem de {}'.format(cont.name),
        from_email=cont.email,
        recipients=(settings.DEFAULT_FROM_EMAIL, cont.email),
        template_name='contact/contact_email.txt',
        context={'contact': cont},
    )

    return HttpResponseRedirect(r('contact'))


def new(request, form=ContactForm()):
    return render(request, 'contact/contact_form.html', {'form': form})


def _send_email(subject, from_email, recipients, template_name, context):
    message = render_to_string(template_name, context)
    mail.send_mail(subject, message, from_email, recipients)
