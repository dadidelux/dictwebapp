from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = "main/base.html"
    context = {
        "name": "Bryan Dadiz",
    }
    return render(request, template, context)


def contact_us(request):
    template = "content/contactus.html"
    context = {
        "name": "Bryan Dadiz",
        "agency": "DICT",
        "description": """
                                The Department of Information and Communications 
                                Technology is the executive department of the Philippine government 
                                responsible for the planning, development and promotion of the 
                                country's information and communications technology agenda in 
                                support of national development.
                        """,
        "address": "3JF6+9Q3, Ramon Magsaysay Ave, Poblacion District, Davao City, 8000 Davao del Sur",
        "hours": "Open now",
        "phone": "(082) 224 5803",
        "depex": "Ivan John Uy, Secretary",
        "founded": "June 9, 2016",
        "childagency": """
                        Cybercrime Investigation and Coordination Center; 
                        National Privacy Commission; National Telecommunications Commission
                        """,
        "country": "Philippines",
        "budget": "₱8.29 billion (2023)",
    }
    return render(request, template, context)
