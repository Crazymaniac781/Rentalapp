from django.shortcuts import render
from .models import RentalHome

def home_list(request):
    rentals = RentalHome.objects.filter(available=True)
    return render(request, 'rentalapp/home_list.html', {'rentals': rentals})
