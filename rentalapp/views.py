from django.shortcuts import render, redirect
from .models import RentalHome, Comment
from .forms import RentalHomeForm, CommentForm

def home_list(request):
    rentals = RentalHome.objects.filter(available=True)
    
    title_query = request.GET.get('q')
    location_query = request.GET.get('location')
    bedrooms_query = request.GET.get('bedrooms')

    if title_query:
        rentals = rentals.filter(title__icontains=title_query)
    if location_query:
        rentals = rentals.filter(location__icontains=location_query)
    if bedrooms_query:
        rentals = rentals.filter(bedrooms=bedrooms_query)

    return render(request, 'rentalapp/home_list.html', {
        'rentals': rentals,
        'title_query': title_query,
        'location_query': location_query,
        'bedrooms_query': bedrooms_query,
    })

def add_rental(request):
    if request.method == 'POST':
        form = RentalHomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_list')
    else:
        form = RentalHomeForm()
    return render(request, 'rentalapp/add_rental.html', {'form': form})

def rental_detail(request, pk):
    rental = RentalHome.objects.get(pk=pk)
    comments = rental.comments.all().order_by('-timestamp')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rental = rental
            comment.save()
            return redirect('rental_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'rentalapp/rental_detail.html', {
        'rental': rental,
        'form': form,
        'comments': comments
    })