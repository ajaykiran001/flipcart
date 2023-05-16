from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sell(request):
    return render(request,'sellers/sell.html')
