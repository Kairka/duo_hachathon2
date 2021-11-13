from django.db import models
from django.urls import reverse

from account.models import User


class Region(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='regions', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name
    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='tours')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tours')
    post = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Image(models.Model):
    image = models.ImageField(upload_to='tours')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url