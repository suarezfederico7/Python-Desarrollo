from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from inicio.models import Avatar

class FormRegistro(UserCreationForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(required=True, label='Nombre')
    last_name = forms.CharField(required=True, label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,help_text = 'Minimo 8 caracteres, 1 numero, 1 caracter especial')
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['username'].widget.attrs.update({'autocomplete': 'new-username'})
        self.fields['first_name'].widget.attrs.update({'autocomplete': 'new-first_name'})
        self.fields['last_name'].widget.attrs.update({'autocomplete': 'new-last_name'})
        self.fields['email'].widget.attrs.update({'autocomplete': 'new-email'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password'})
        self.fields['password2'].widget.attrs.update({'autocomplete': 'new-password'})    

class FormModificacion(UserChangeForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='Nombre')
    last_name = forms.CharField(required=True, label='Apellido')

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']