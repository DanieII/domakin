from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

from allauth.account.forms import SignupForm, LoginForm

UserModel = get_user_model()


class UserRegisterForm(SignupForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input input-bordered", "placeholder": "Име"}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"] = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "autofocus": True,
                    "class": "input input-bordered",
                    "placeholder": "Имейл",
                    "type": "email",
                }
            )
        )
        self.fields["password1"] = forms.CharField(
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                    "autocomplete": "new-password",
                    "class": "input input-bordered",
                    "placeholder": "Парола",
                }
            ),
        )
        self.fields["password2"] = forms.CharField(
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                    "autocomplete": "new-password",
                    "class": "input input-bordered",
                    "placeholder": "Повтори паролата",
                }
            ),
        )


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"] = UsernameField(
            widget=forms.EmailInput(
                attrs={
                    "autofocus": True,
                    "class": "input input-bordered",
                    "placeholder": "Имейл",
                    "type": "email",
                }
            )
        )
        self.fields["password"] = forms.CharField(
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                    "autocomplete": "current-password",
                    "class": "input input-bordered",
                    "placeholder": "Парола",
                }
            ),
        )
        self.fields["remember"] = forms.BooleanField(
            label="Запомни ме",
            required=False,
            widget=forms.CheckboxInput(attrs={"class": "checkbox"}),
        )
