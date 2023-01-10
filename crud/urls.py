from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerPerson', views.registerPerson),
    path('deletePerson/<person_id>', views.deletePerson),
    path('editPerson/<person_id>', views.editPerson),
    path('confirmedEditPerson', views.confirmedEditPerson)
]