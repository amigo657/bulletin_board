from django.shortcuts import render

def blog_page(request):
    return render(request, "blog_home.html", {})

def blog_details(request):
    return render(request, "blog_details.html", {})