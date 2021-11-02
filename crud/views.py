from django.shortcuts import render, redirect
from crud.models import Vehicles


# Create your views here.
def index(request):
    vhc =Vehicles.objects.all()
    context = {'vhc':vhc}
    return render(request,'index.html',context)

def add(request):
    if request.method =="POST":
        name=request.POST.get('name')
        description = request.POST.get('description')
        vhc =Vehicles(name=name, description=description)
        vhc.save()
        return redirect('home')
    return render(request,'index.html')

def edit(request):
    vhc = Vehicles.objects.all()
    context = {'vhc': vhc}
    return redirect(request, 'index.html',context)

def update(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        vhc = Vehicles(id=id,name=name, description=description)
        vhc.save()
        return redirect('home')
    return redirect(request, 'index.html')

def delete(request,id):
    vhc = Vehicles.objects.filter(id=id)
    vhc.delete()
    context = {'vhc': vhc}
    return redirect('home')


