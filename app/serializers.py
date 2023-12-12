from rest_framework.serializers import ModelSerializer

from app.models import Receipt


class ReceiptSerializer(ModelSerializer):
    class Meta:
        model = Receipt
        fields = "__all__"