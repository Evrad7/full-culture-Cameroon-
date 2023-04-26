from django import forms
from .models import Comment


class CommentAdminForm(forms.ModelForm):

    class Meta:
        fields = ["author", "content"]
        model = Comment
        widgets = {
            "content": forms.Textarea(attrs={"cols": 70, "rows": 5})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        fields = ["article", "author", "content"]
        model = Comment
        widgets = {
            "content": forms.Textarea()
        }
