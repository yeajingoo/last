from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def holy(request):
    return render(request, 'holy.html')
    
def create(request):
    return render(request, 'creat.html')

def list(request):
    return render(request, 'list.html')