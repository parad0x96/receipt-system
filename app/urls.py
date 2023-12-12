from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from app.views import ReceiptViewSet, sign_up

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", sign_up, name="signup"),
    path(
        "receipts/",
        ReceiptViewSet.as_view({"get": "list", "post": "create"}),
        name="receipt-list",
    ),
    path(
        "receipts/<int:pk>/",
        ReceiptViewSet.as_view({"get": "retrieve"}),
        name="receipt-detail",
    ),
    path(
        "receipts/create/",
        ReceiptViewSet.as_view({"get": "create", "post": "create"}),
        name="receipt-create",
    ),
    path(
        "receipts/<int:pk>/update/",
        ReceiptViewSet.as_view({"post": "update", "get": "update"}),
        name="receipt-update",
    ),
    path(
        "receipts/<int:pk>/delete/",
        ReceiptViewSet.as_view({"delete": "destroy", "get": "destroy"}),
        name="receipt-delete",
    ),
]
