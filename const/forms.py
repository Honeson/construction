from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Your Name',
        'id': 'name'
    }), error_messages={
        'required': 'Please provide your name!'
    })
    email = forms.EmailField(max_length=50, widget=forms.TextInput({
        'class':'form-control',
        'placeholder': 'Your Email Address',
        'id': 'email'
    }))
    msg = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Your message here',
        'id': 'msg'
    }))