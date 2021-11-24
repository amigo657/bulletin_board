from django import forms
# from django.contrib.auth import login as log_in, authenticate
from users.models import User


# class UserLogIn(forms.Form):
#     username = forms.CharField(
#         label = 'User name',
#         widget = forms.TextInput(
#             attrs = {
#                 "id": "name",
#                 "class": "form-control",
#                 "placeholder": "User name",
#                 "onfoces": "this.placeholder = ''",
#                 "onblur": "this.placeholder = 'User name'"
#             }
#         ),
#     )
#     password = forms.CharField(
#         label = "Password",
#         widget = forms.PasswordInput(
#             attrs = {
#                 "id": "password",
#                 "class": "form-control",
#                 "placeholder": "Password",
#                 "onfoces": "this.placeholder = ''",
#                 "onblur": "this.placeholder = 'Password'"
#             }
#         ),
#     )

#     def cleane(self):
#         user = authenticate(**dict(self.cleaned_data))
#         if user is not None:
#             self.user = user
#             return self.cleaned_data, self.user
#         else:
#             self.add_error("username", "Неверный пользователь")
#             self.add_error("password", "Неверный пароль")
#             raise forms.ValidationError("Пользователь не определен")

#     def login(self, request):
#         log_in(request.user)