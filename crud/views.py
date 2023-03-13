from django.shortcuts import render, redirect
from .models import Member


def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add_form(request):
    return render(request, 'add_form.html')

def add_rec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member(first_name = x, last_name = y, country = z)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def upd_rec(request, id):
    mem = Member.objects.get(id=id)
    mem.first_name = request.POST['first']
    mem.last_name = request.POST['last']
    mem.country = request.POST['country']
    mem.save()
    return redirect('/')
    