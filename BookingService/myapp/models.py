from django.db import models

class Room(models.Model):
    price = models.FloatField()
    occupied = models.BooleanField()
    number = models.IntegerField()

    def __str__(self):
        return "No. {} ------ Price: {} ------ Occupied: {}".format(self.number, self.price, self.occupied)

class Reservation(models.Model):
    dateFrom = models.DateField()
    dataTo = models.DateField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return "From: {} ------ To: {}".format(self.dateFrom, self.dataTo)

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.IntegerField()

    def __str__(self):
        return "{} {} ------ Phone: {}".format(self.first_name, self.last_name, self.phone_number)