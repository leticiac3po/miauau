from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.submit_img, name = 'submit'),
    path('result/', views.result, name = 'result'),
    path('gallery/', views.gallery, name = 'gallery')
]