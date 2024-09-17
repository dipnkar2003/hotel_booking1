from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Amenities , Hotel
from django.db.models import Q
# Create your views here.

def home(request):
    amenity_obj = Amenities.objects.all()
    hotel_obj = Hotel.objects.all()
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenity = request.GET.getlist('amenities')
    print(amenity)
    if sort_by:
        if sort_by == 'ASC':
            print('sort')
            hotel_obj = hotel_obj.order_by('hotel_price')
        elif sort_by == 'DSC':
            print('not sort')
            hotel_obj = hotel_obj.order_by('-hotel_price')

    if search :
           hotel_obj = hotel_obj.filter(
               Q(hotel_name__icontains = search)|
               Q(description__icontains = search)
               )
        
    if len(amenity):
        hotel_obj = hotel_obj.filter(amenities__amenity_name__in =  amenity)

    context = {'amenity_obj':amenity_obj , 'hotel_obj':hotel_obj , 'sort_by':sort_by ,'search':search , 'amenities':amenity}
    return render(request, 'hotel.html' , context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        user_obj = User.objects.filter(username = username)
        print(user_obj)
        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = authenticate(request , username = username , password = password)
        if not user:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request , user)
        return redirect('/')
    return render(request ,'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()
        return redirect('/login_page')

    return render(request , 'register.html')

def hotel_detail(request , uid):
    hotel_obj = Hotel.objects.get(uid = uid)
    return render(request ,'hotel_detail.html' ,{'hotel_obj':hotel_obj} )