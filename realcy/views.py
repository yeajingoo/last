from django.shortcuts import render, redirect

# Create your views here.
def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')
    
def third(request):
    return render(request, 'third.html')
    
def forth(request):
    return render(request, 'forth.html')

def fifth(request):
    if request.method == "POST":
        name = request.POST.get('name')
        redirect('fifth')
    return render(request, 'fifth.html', {'name': name})