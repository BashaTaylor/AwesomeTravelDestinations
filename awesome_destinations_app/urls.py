# urls.py
from django.urls import path
from . import views
from .views import contact_form

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('travel_blog/', views.travel_blog, name='travel_blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('search_results/', views.search_results, name='search_results'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('destination/<int:id>/edit/', views.edit_destination, name='edit_destination'),
    path('destination/<int:id>/delete/', views.delete_destination, name='delete_destination'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('contact/', contact_form, name='contact_form'),
    path('success/', views.success, name='success'),  # Success page URL
    # other paths...
]
