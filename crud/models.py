from django.db import models

# Create your models here.
class AddressBook(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} ({self.person_id})'