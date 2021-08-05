from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        error_messages={
            "required": "Your name cannot be null",
        }
    )
    password = forms.CharField(
        label="Your password", 
        max_length=128, 
        widget=forms.PasswordInput(),
        error_messages={
            "required": "Your password cannot be null",
        }
    )