from django.shortcuts import get_object_or_404, render
from value.models import MBook
# Create your views here.
def book_detail(request,pk):
    booka=get_object_or_404(MBook,pk=pk)
    context={
        'booka':booka,
    }
    return render (request,'book_detail.html',context)