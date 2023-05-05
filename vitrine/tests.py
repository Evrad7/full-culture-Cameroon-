from django.test import TestCase, Client
from django.conf import settings
from .models import Company, Contact, ContactForNewLetter

# Create your tests here.


class TestCaseContact(TestCase):
    def setUp(self):
        Company.objects.create(name="AfrikDesign", description="Meilleur des entreprises", email="afrikdesign@gmail.com",
                               phone1="674528565", phone2="697851254", address="Douala/Cameroun", slogan="Toujours plus loin")
        self.client = Client()

    def test_case_send_message(self):
        url = "/fr/contact-post/"
        pre_count = Contact.objects.count()
        response = self.client.post(url, {"name": "Castor", "email": "castor@gmail.com", "subject": "Demande de rencontre",
                                          "description": "J'aimarai rencontrer votre telentueuse équipe pour un projet"})
        post_count = Contact.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(pre_count+1, post_count)

    def test_case_send_many_messages(self):
        url = "/fr/contact-post/"
        number = settings.THROTTLE_ZONES["contact"]["BUCKET_CAPACITY"]
        for _ in range(number+1):
            try:
                self.client.post(url, {"name": "Castor", "email": "castor@gmail.com", "subject": "Demande de rencontre",
                                       "description": "J'aimarai rencontrer votre telentueuse équipe pour un projet"})
            except:
                break

        if _ == number-1:
            self.assertFalse(True)


class TestCaseNewsLetter(TestCase):
    def setUp(self):
        Company.objects.create(name="AfrikDesign", description="Meilleur des entreprises", email="afrikdesign@gmail.com",
                               phone1="674528565", phone2="697851254", address="Douala/Cameroun", slogan="Toujours plus loin")
        self.client = Client()

    def test_case_many_subscription_to_newsletter(self):
        url = "/fr/subscribe-newsletter/"
        pre_count = ContactForNewLetter.objects.count()
        number = settings.THROTTLE_ZONES["newsletter"]["BUCKET_CAPACITY"]
        for _ in range(number+1):
            try:
                response = self.client.post(
                    url, {"email": f"subscriptor{_}@gmail.com"})
            except:
                break
        if _ == number-1:
            self.assertFalse(True)

    def test_case_subscription_to_newsletter(self):
        url = "/fr/subscribe-newsletter/"
        pre_count = ContactForNewLetter.objects.count()
        response = self.client.post(url, {"email": "subscriptor@gmail.com"})
        post_count = ContactForNewLetter.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(pre_count+1, post_count)
