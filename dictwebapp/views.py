from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = "main/base.html"
    context = {
            "name":"Bryan Dadiz",
    }
    return render(request, template, context)




