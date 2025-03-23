from django.contrib import admin
from .models import RentalHome, Comment

@admin.register(RentalHome)
class RentalHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'bedrooms', 'bathrooms', 'available')
    list_filter = ('available', 'location')
    search_fields = ('title', 'location', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rental', 'timestamp')
    search_fields = ('name', 'message')
    list_filter = ('timestamp',)
