from django.contrib import admin
from app.models import Receipt

# Register your models here.


class ReceiptAdmin(admin.ModelAdmin):
    readonly_fields = ("date_of_purchase",)
    list_display = ("id", "date_of_purchase", "total_amount", "user")


admin.site.register(Receipt, ReceiptAdmin)
