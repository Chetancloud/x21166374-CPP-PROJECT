from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
     # Create your views here.
def index(request):
    return HttpResponse("You're at the preloans index.")
    
def about(request):
    context = {}
    return render(request, 'preloans/about.html', context)

#def main(request):
  #  context = {}
#    return render(request, 'preloans/main.html', context)
    
def preloans(request):
    context = {}
    return render(request, 'preloans/preloans.html', context)
    
def services(request):
    context = {}
    return render(request, 'preloans/services.html', context)
    
def contacts(request):
    context = {}
    return render(request, 'preloans/contacts.html', context)
    
def carloan(request):
    context = {}
    return render(request, 'preloans/carloan.html', context)

def eduloan(request):
    context = {}
    return render(request, 'preloans/eduloan.html', context)

def homeloan(request):
    context = {}
    return render(request, 'preloans/homeloan.html', context)
    
def personalloan(request):
    context = {}
    return render(request, 'preloans/personalloan.html', context)
    

    


    

    