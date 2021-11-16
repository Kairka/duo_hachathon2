from datetime import datetime

from django import forms

from .models import Tour, Image, Comment


class TourForm(forms.ModelForm):
    post = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Tour
        exclude = ('user', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

