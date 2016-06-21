from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class LoginForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("User does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")
        return super(LoginForm, self).clean(*args, **kwargs)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
            

