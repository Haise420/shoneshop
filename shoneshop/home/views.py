from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):

    proizvodi = Proizvod.objects.all()

    if request.method == 'POST':
        ime = request.POST.get('ime')
        deskripcija = request.POST.get('deskripcija')
        cena = request.POST.get('cena')
        kolicina = request.POST.get('kolicina')
        slika = request.POST.FILES['image']

        novi_proizvod = Proizvod(ime=ime, deskripcija=deskripcija, cena=cena, kolicina=kolicina, image=slika)
        novi_proizvod.save()

        return redirect('home')



    context = {'proizvodi': proizvodi}

    return render(request, 'home/home.html', context)


def delete_proizvod(request, proizvod_id):
    if request.method == 'POST':
        proizvod = Proizvod.objects.get(id=proizvod_id)
        proizvod.delete()
        return redirect('home')
