from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Receipt


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sign_up_view(self):
        url = reverse("signup")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")

    def test_sign_up_view_post(self):
        url = reverse("signup")
        response = self.client.post(
            url,
            data={
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("receipt-list"))
        self.assertEqual(User.objects.count(), 1)


class ReceiptViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.receipt = Receipt.objects.create(
            user=self.user, store_name="Test Store", total_amount=10.0
        )

    def test_receipt_list(self):
        url = reverse("receipt-list")
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receipt/receipt_list.html")

    def test_receipt_retrieve(self):
        url = reverse("receipt-detail", kwargs={"pk": self.receipt.pk})
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receipt/receipt_detail.html")

    def test_receipt_create(self):
        url = reverse("receipt-create")
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receipt/receipt_form.html")

        data = {
            "store_name": "New Store",
            "total_amount": 20.0,
            "item_list": "item1,item2",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("receipt-list"))
        self.assertEqual(Receipt.objects.count(), 2)

    def test_receipt_update(self):
        url = reverse("receipt-update", kwargs={"pk": self.receipt.pk})
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receipt/receipt_form.html")

        data = {
            "store_name": "Updated Store",
            "total_amount": 90.5,
            "item_list": "item3,item4",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("receipt-list"))
        self.receipt.refresh_from_db()
        self.assertEqual(self.receipt.store_name, "Updated Store")

    def test_receipt_delete(self):
        url = reverse("receipt-delete", kwargs={"pk": self.receipt.pk})
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("receipt-list"))
        self.assertEqual(Receipt.objects.count(), 0)
