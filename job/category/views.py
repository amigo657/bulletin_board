from django.shortcuts import render

def category_page(request):
    return render(request, "category_page.html", {})
