from django.db import models

# Create your models here.


class Sales(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    mail_id = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    college = models.CharField(max_length=30)
    pay_mode = models.CharField(max_length=6)
    location_sale = models.CharField(max_length=15)
    amount = models.CharField(max_length=5)
    event_name = models.CharField(max_length=30)
    sale_type = models.CharField(max_length=15)
    pch_name = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=128)
    time = models.DateTimeField()

    # ...
    def __str__(self):
        return self.name
