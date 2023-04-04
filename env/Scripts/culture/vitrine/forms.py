from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["subject"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control"})

    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "description"]
