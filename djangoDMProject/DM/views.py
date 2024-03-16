from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Inventory, ChangeLog
from django.http import HttpResponseRedirect, HttpResponseNotFound


def index(request):
    change_log = ChangeLog.objects.all()
    return render(request, 'DM/index.html', {"change_log": change_log})


def main(request):
    try:
        if request.method == "POST":
            inventory_write = Inventory.objects.get(player=request.session["id"])
            inventory_write.gold = request.POST.get("gold")
            inventory_write.hp = request.POST.get("hp")
            inventory_write.save()

        current_user = request.session["username"]
        inventory = Inventory.objects.get(player=request.session["id"])
        return render(request, 'DM/main.html', {"current_user": current_user, "inv": inventory})
    except KeyError:
        return HttpResponseRedirect('/dma/')


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = User.objects.create_user(username=name, password=password)
        Inventory.objects.create(player=user)
        request.session["id"] = user.id
        request.session["username"] = user.name
        user.save()
        return HttpResponseRedirect('/dma/')

    return render(request, 'DM/register.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user is not None:
            request.session["id"] = user.id
            request.session["username"] = user.username
            return HttpResponseRedirect('/dma/')
        else:
            return HttpResponseNotFound("User not found")

    return render(request, 'DM/login.html')
