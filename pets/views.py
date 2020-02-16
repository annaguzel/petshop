from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm


# Create your views here.
def pet_list(request):
    petlist =[]
    for item in Pet.objects.all():
        if item.available == True:
            petlist.append(item)
    context = {
        "pets": petlist
    }
    return render(request, 'petlist.html', context)

def pet_detail(request, pet_id):
    context = {
        "pet":Pet.objects.get(id = pet_id)
    }
    return render(request , 'petdetail.html', context)

def create_pet(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'createpet.html', context)

def update_pet(request, pet_id):
    pet= Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet)
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES,instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "pet":pet,
        "form":form,
    }
    return render(request, 'updatepet.html', context)

def delete_pet(request, pet_id):
    Pet.objects.get(id=pet_id).delete()

    return redirect('pet-list')
