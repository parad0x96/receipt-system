from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipt(models.Model):
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    item_list = models.TextField()
    total_amount = models.FloatField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)