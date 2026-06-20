from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse(""" 
                        <h1> hello  world </h1>
                        <p>yuguygyjyu</p>
                        
                        """)


def faq(request):
    return render(request, "index.html")

def products(request):
    
    heading = "This is Products page heading"
    productsList  = [
        {'id':1, 'name':"IPhone", 'img':"https://images.unsplash.com/photo-1726574686436-5ef90358e032?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aXBob25lJTIwMTN8ZW58MHx8MHx8fDA%3D"},
        {'id':2, 'name':'Samsung', 'img':"https://images.samsung.com/is/image/samsung/p6pim/in/s2602/gallery/in-galaxy-s26-ultra-s948-sm-s948bzvbins-thumb-550793679"},
        {'id':3, 'name':'VIVO', 'img':'https://images.unsplash.com/photo-1755318535396-cdb062dc60bd?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dml2byUyMHNtYXJ0cGhvbmV8ZW58MHx8MHx8fDA%3D'}
    ]
    
    return render(request, "products/index.html", context={'heading':heading , 'products':productsList } )

def details(request,id):

    productsList  = [
        {'id':1, 'name':"IPhone", 'img':"https://images.unsplash.com/photo-1726574686436-5ef90358e032?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aXBob25lJTIwMTN8ZW58MHx8MHx8fDA%3D"},
        {'id':2, 'name':'Samsung', 'img':"https://images.samsung.com/is/image/samsung/p6pim/in/s2602/gallery/in-galaxy-s26-ultra-s948-sm-s948bzvbins-thumb-550793679"},
        {'id':3, 'name':'VIVO', 'img':'https://images.unsplash.com/photo-1755318535396-cdb062dc60bd?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dml2byUyMHNtYXJ0cGhvbmV8ZW58MHx8MHx8fDA%3D'}
    ]

    selectedProduct=productsList

    for product in productsList:
        if product["id"]==id:
            selectedProduct=product


    return render(request, "products/details.html", context={"product":selectedProduct})