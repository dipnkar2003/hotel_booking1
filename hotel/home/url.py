
from django.contrib import admin
from django.urls import path
from .views import home , login_page , register_page , hotel_detail
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('' , home , name='home'),
    path('login_page' , login_page , name='login_page'),
    path('register_page' , register_page , name='register_page'),
    path('hotel-detail/<uid>' , hotel_detail,  name = 'hotel_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()    




