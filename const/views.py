from django.views.generic import TemplateView, View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm
# Create your views here.



class HomePageView(TemplateView):
    template_name = 'home.html'

def HomePage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            try:
                send_mail(subject, message, from_email, ['sunny@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! We have received your message and will get back shortly',\
                'sunny@exmaple.com', [from_email] )
            #messages.info(request, 'Congratulations')
            return redirect('success')
        messages.warning(request, 'Please Go Back To The Form And Correct Your Error...')
    return render(request, 'home.html', {'form': form})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            form.save()
            try:
                send_mail(subject, message, from_email, ['sunny@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! We have received your message and will get back shortly',\
                'sunny@exmaple.com', [from_email] )
            #messages.info(request, 'Congratulations')
            #return redirect('success')
            messages.info(request, 'Congratulations')
            
    return render(request, 'email.html', {'form': form})

'''
class ContactView(View):
    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', 'New Message from name')
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            try:
                send_mail(subject, message, from_email, ['sunny@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(self.request, 'Congratulations')
            return redirect('success')
        #return render(request, 'home.html', {'form': form})
 '''   

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    messages.info(request, 'Thank you for contacting us, We\'ll get in touch...')
    return redirect('home')