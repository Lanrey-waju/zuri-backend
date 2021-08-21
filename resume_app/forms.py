from django import forms
from django.db.models import fields
from .models import UserMessage
from django.core.exceptions import ValidationError

# Create a Contact Me form
class Message_me(forms.ModelForm):
    class Meta:
        model = UserMessage
        # fields = "__all__"
        exclude = ["date_received"]

    # def clean_subject(self):
    #     subject = self.cleaned_data.get("subject")
    #     print(subject)
    #     if subject in [entry.subject for entry in UserMessage.objects.all()]:
    #         raise ValidationError("Subject already exists")
    #     return subject
