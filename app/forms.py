from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Receipt


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["store_name", "item_list", "total_amount"]
