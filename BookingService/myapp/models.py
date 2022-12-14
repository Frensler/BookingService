from django.db import models

class Room(models.Model):
    price = models.FloatField()
    occupied = models.BooleanField()
    number = models.IntegerField()

    def __str__(self):
        return "No. {} ------ Price: {} ------ Occupied: {}".format(self.number, self.price, self.occupied)
