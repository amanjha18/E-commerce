# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path("",views.index, name='ShopHome'),
    path("about/", views.about, name='About'),
    path("contact/", views.contact, name="Contact us"),
    path("tracker/", views.tracker, name="tracking status"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Productview"), 
    path("checkout/", views.checkout, name="Checkout"),
    

]
