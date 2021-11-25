from django import forms
from django.contrib.auth import login as log_in, authenticate
from users.models import User


class UserSignIn(forms.Form):
    username = forms.CharField(
        label = "User name",
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class":"form-control",
                "placeholder": "User name",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'"
            }
        ),
    )
    email = forms.EmailField(
        label = "Email",
        widget = forms.TextInput(
            attrs = {
                "id": "email",
                "class":"form-control",
                "placeholder": "User email",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User email'"
            }
        ),
    )
    first_name = forms.CharField(
        label = "First name",
        widget = forms.TextInput(
            attrs = {
                "id": "first_name",
                "class":"form-control",
                "placeholder": "First name",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'First name'"
            }
        ),
    )
    last_name = forms.CharField(
        label = "Last name",
        widget = forms.TextInput(
            attrs = {
                "id": "last_name",
                "class":"form-control",
                "placeholder": "Last name",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Last name'"
            }
        ),
    )
    password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(
            attrs = {
                "id": "password",
                "class":"form-control",
                "placeholder": "Password",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'"
            }
        ),
    )
    repeat_password = forms.CharField(
        label = "Repeat_password",
        widget = forms.PasswordInput(
            attrs = {
                "id": "repeat_password",
                "class":"form-control",
                "placeholder": "Repeat password",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Repeat_password'"
            }
        ),
    )
    is_agree = forms.BooleanField(
        label = "Is agree",
        widget = forms.CheckboxInput(
            attrs = {
                "id": "is_agree",
                "class": "form-control",
            }
        ),
    )

    def clean(self):
        is_error = False
        try:
            tmp_user = User.objects.get(username = self.cleaned_data["username"])
        except User.DoesNotExist:
            print("Ошибка")
        else:
            self.add_error("username", "Такой пользователь уже существует")
            is_error = True
        if self.cleaned_data["password"] != self.cleaned_data["repeat_password"]:
            self.add_error("password", "Пароли не совпадают !")
            self.add_error("repeat_password", "Пароли не совпадают !")
        if not self.cleaned_data["is_agree"]:
            self.add_error("is_error", "Необходимо ваше согласие")
            is_error = True
        if is_error:
            raise forms.ValidationError("Проверьте корректность введенных данных")
        return super().clean()
    
    def save(self):
        new_user = User(
            username = self.cleaned_data["username"],
            email = self.cleaned_data["email"],
            first_name = self.cleaned_data["first_name"],
            last_name = self.cleaned_data["last_name"],
            password = self.cleaned_data["password"],
        )
        new_user.save()

class UserLogIn(forms.Form):
    username = forms.CharField(
        label = 'User name',
        widget = forms.TextInput(
            attrs = {
                "id": "name",
                "class": "form-control",
                "placeholder": "User name",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'"
            }
        ),
    )
    password = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput(
            attrs = {
                "id": "password",
                "class": "form-control",
                "placeholder": "Password",
                "onfoces": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'"
            }
        ),
    )

    def cleane(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data, self.user
        else:
            self.add_error("username", "Неверный пользователь")
            self.add_error("password", "Неверный пароль")
            raise forms.ValidationError("Пользователь не определен")

    def login(self, request):
        log_in(request.user)