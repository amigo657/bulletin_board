from django.shortcuts import render
from django.shortcuts import redirect
from home.forms import LinkForm

def home_page(request):
    link = {"form": LinkForm()}
    if request.method == "POST":
        email_form = LinkForm(request.POST)
        if email_form.is_valid():
            email_form.save()
            return redirect("home")
        link.update(form=email_form)
    return render(request, "home_page.html", link)

# def link_em(request):
#     link = {"form": LinkForm()}
#     print(link)
#     if request.method == "POST":
#         email_form = LinkForm(request.POST)
#         if email_form.is_valid():
#             email_form.save()
#             return redirect("home")
#         link.update(form=email_form)
#     return render(request, "home_page.html", link)
