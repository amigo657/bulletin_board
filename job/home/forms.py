from django import forms
from home.models import Link


class LinkForm(forms.Form):
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "id": "email",
                "class":"form-control",
                "placeholder": "Your email here",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Email'"
            }
        ),
    )

    def clean(self):
        is_error = False
        try:
            tmp_user = Link.objects.get(email = self.cleaned_data["email"])
        except Link.DoesNotExist:
            print("Ошибка")
        return super().clean()

    def save(self):
        new_email = Link(email = self.cleaned_data["email"])
        new_email.save()


    # def save(self):
    #     new_email = Link(self.email)
    #     new_email.save()