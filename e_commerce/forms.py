from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        error_messages={'required':'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Nome completo",
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid':'Digite um e-mail válido'},
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder": "E-mail",
            }
        )
    )
    content = forms.CharField(
        error_messages={'required':'Obrigatório o preenchimento da mensagem'},
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder": "Digite sua mensagem",
            }
        )
    )

    ''' def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError("O e-mail precisa ser do gmail.com")
        return email '''