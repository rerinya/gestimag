
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image/<int:id>', views.image, name='image'),
    path('add_images', views.add_images, name='add_images'),
    path('delete/<int:id>', views.delete_image, name='delete'),
]
