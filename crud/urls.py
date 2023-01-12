from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('registerPerson', views.registerPerson),
    path('home/deletePerson/<person_id>', views.deletePerson),
    path('home/editPerson/<person_id>', views.editPerson),
    path('confirmedEditPerson', views.confirmedEditPerson)
]