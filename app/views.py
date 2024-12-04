from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'sunny','age':20,'course':'pythonfullstack'}
    return render(request,'conditions.html',context=d)
