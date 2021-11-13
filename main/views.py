from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TourForm, ImageForm
from .models import *


def index(request):
    return render(request, 'index.html')

def region_detail(request, slug):
    region = Region.objects.get(slug=slug)
    tours = Tour.objects.filter(region_id=slug)
    return render(request, 'region_detail.html', locals())


def detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    images = tour.images.all()
    return render(request, 'tour_detail.html', locals())


def add_tour(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        tour_form = TourForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if tour_form.is_valid() and formset.is_valid():
            tour = tour_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, tour=tour)

            return redirect(tour.get_absolute_url())
    else:
        tour_form = TourForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add-tour.html', locals())


def update_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    tour_form = TourForm(request.POST or None, instance=tour)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(tour=tour))
    if tour_form.is_valid() and formset.is_valid():
        tour = tour_form.save()

        for form in formset:
            image = form.save(commit=False)
            image.tour = tour
            image.save()
            return redirect(tour.get_absolute_url())
    return render(request, 'update-tour.html', locals())


def delete_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        tour.delete()
        messages.add_message(request, messages.SUCCESS, 'You are successfully deleted tour')
        return redirect('home')
    return render(request, 'delete-tour.html', locals())



