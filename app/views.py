from app.models import Receipt
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import redirect, render
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated

from app.serializers import ReceiptSerializer
from app.forms import ReceiptForm, SignUpForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect("receipts")
    else:
        form = SignUpForm()
    return render(request, "account/signup.html", {"form": form})


class ReceiptViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "receipt/receipt_list.html"
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response({"receipts": queryset})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(
            {"receipt": instance}, template_name="receipt/receipt_detail.html"
        )

    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ReceiptForm(request.POST)
            if form.is_valid():
                receipt = form.save(commit=False)
                receipt.user = request.user
                receipt.save()
                return redirect("receipt-list")
        else:
            form = ReceiptForm()
        return render(request, "receipt/receipt_form.html", {"form": form})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        form = ReceiptForm(request.POST or None, instance=instance)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("receipt-list")
        return Response(
            {"form": form, "instance": instance},
            template_name="receipt/receipt_form.html",
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return redirect("receipt-list")
