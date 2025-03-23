from django.shortcuts import render, redirect
from .models import RentalHome
from .forms import RentalHomeForm

def home_list(request):
    rentals = RentalHome.objects.filter(available=True)
    return render(request, 'rentalapp/home_list.html', {'rentals': rentals})

def add_rental(request):
    if request.method == 'POST':
        form = RentalHomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_list')
    else:
        form = RentalHomeForm()
    return render(request, 'rentalapp/add_rental.html', {'form': form})
