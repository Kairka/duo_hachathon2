from datetime import datetime

from django import forms

from .models import Tour, Image


class TourForm(forms.ModelForm):
    post = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Tour
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )