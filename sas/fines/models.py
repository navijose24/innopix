from django.db import models

class Fine(models.Model):
    vehicle_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)  # Client's phone number
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        choices=[("unpaid", "Unpaid"), ("paid", "Paid")],
        max_length=10,
        default="unpaid",
    )
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fine: {self.vehicle_number} - {self.amount} ({self.status})"



class VehicleOwner(models.Model):
    vehicle_type = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20, unique=True)
    owner_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    fine_status=models.CharField(max_length=20,default="Unpaid")

    def _str_(self):
        return f"{self.vehicle_type} - {self.number_plate}"