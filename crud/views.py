from django.shortcuts import render, redirect
from .models import AddressBook
from django.contrib import messages
from .utils import validateEmail


def home(request):
    if not request.user.is_authenticated:
        messages.success(request, ('You have to be logged in!'))
        return redirect('login')
    else:
        addresses = AddressBook.objects.all()
        return render(request, "address_book.html", {'addresses':addresses})

def registerPerson(request):
    errors = []
    name = request.POST['txtName']
    email = request.POST['txtEmail']
    address = request.POST['txtAddress']
    phone_number = request.POST['txtPhoneNumber']

    errors = validateEmail(email)
    if len(errors) > 0:
        messages.success(request, errors[0])
    else:
        person = AddressBook.objects.create(name=name, email=email, address=address, phone_number=phone_number)
    return redirect('home')

def confirmedEditPerson(request):
    person_id = request.POST['numPersonId']
    name = request.POST['txtName']
    email = request.POST['txtEmail']
    address = request.POST['txtAddress']
    phone_number = request.POST['txtPhoneNumber']
    person = AddressBook.objects.get(person_id=person_id)
    
    errors = validateEmail(email)
    if len(errors) > 0:
        messages.success(request, errors[0])
        return render(request, 'editPerson.html', {'person':person})

    person.name = name
    person.email = email
    person.address = address
    person.phone_number = phone_number
    person.save()
    return redirect('home')

def editPerson(request, person_id):
    person = AddressBook.objects.get(person_id=person_id)
    return render(request, 'editPerson.html', {'person':person})

def deletePerson(request, person_id):
    person = AddressBook.objects.get(person_id=person_id)
    person.delete()
    return redirect('home')
