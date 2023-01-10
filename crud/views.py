from django.shortcuts import render, redirect
from .models import AddressBook

# Create your views here.
def home(request):
    addresses = AddressBook.objects.all()
    return render(request, "address_book.html", {'addresses':addresses})

def registerPerson(request):
    name = request.POST['txtName']
    email = request.POST['txtEmail']
    address = request.POST['txtAddress']
    phone_number = request.POST['txtPhoneNumber']

    person = AddressBook.objects.create(name=name, email=email, address=address, phone_number=phone_number)
    return redirect('/')

def confirmedEditPerson(request):
    person_id = request.POST['numPersonId']
    name = request.POST['txtName']
    email = request.POST['txtEmail']
    address = request.POST['txtAddress']
    phone_number = request.POST['txtPhoneNumber']
    
    person = AddressBook.objects.get(person_id=person_id)
    person.name = name
    person.email = email
    person.address = address
    person.phone_number = phone_number
    person.save()
    return redirect('/')

def editPerson(request, person_id):
    person = AddressBook.objects.get(person_id=person_id)
    return render(request, 'editPerson.html', {'person':person})

def deletePerson(request, person_id):
    person = AddressBook.objects.get(person_id=person_id)
    person.delete()
    return redirect('/')