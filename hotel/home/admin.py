from django.contrib import admin

# Register your models here.
from .models import Amenities,Hotel,HotelImages,HotelBooking
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)
admin.site.register(Amenities)