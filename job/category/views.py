from django.shortcuts import render
from category.models import Work

def category_page(request):
    works = Work.objects.all()
    return render(request, "category_page.html", {'works': works})
