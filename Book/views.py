from django.shortcuts import render
from value.models import MBook
def details(request):
    book=MBook.objects.all()
    context={
        'book':book,
    }
    return render(request,'home.html',context)
