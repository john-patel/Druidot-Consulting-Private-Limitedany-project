from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    # scheduled_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    scheduled_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y/%m/%d %I:%M:%S'],
        required=False  # Set the field as optional
    )
    class Meta:
        model = UploadedImage
        fields = ('image',)

