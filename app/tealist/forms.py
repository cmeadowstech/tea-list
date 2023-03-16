from django import forms
from .models import comment, vendor


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Please share your thoughts...",
                "rows": 4,
                "cols": 50,
            }
        ),
    )
    value = forms.ChoiceField(label="Rating", choices = comment.value.field.choices)

    class Meta:
        model = comment
        fields = ["content", "value"]

class VendorForm(forms.ModelForm):
    

    class Meta:
        model = vendor
        fields = ["name", "description", "store_location"]
        widgets = {'store_location': forms.CheckboxSelectMultiple}
