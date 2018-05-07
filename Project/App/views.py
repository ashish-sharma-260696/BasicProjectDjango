from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request,'details.html')

def father(request):
    return render(request,'father.html')

def mother(request):
    return render(request,'mother.html')

def children(request):
    return render(request,'children.html')    
