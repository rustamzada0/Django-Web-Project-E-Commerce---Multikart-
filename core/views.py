from django.shortcuts import render, get_object_or_404
from product.models import *
from .models import *

# Create your views here.
def home(request):
    items = Image.objects.filter(variant__is_main_variant=True).filter(is_main=True)

    for i in items:
        print(i.variant.new_status)

    blogs_images = MainPhotos.objects.filter(blog=True)
    insta_images = MainPhotos.objects.filter(insta=True)
    main_photos_men = MainPhotos.objects.get(id=1)
    main_photos_women = MainPhotos.objects.get(id=2)
    men_collection = MainPhotos.objects.get(id=3)
    women_collection = MainPhotos.objects.get(id=4)
    parallax = MainPhotos.objects.get(id=5)

    context = {
        'women_collection':women_collection,
        'men_collection':men_collection,
        'main_photos_men':main_photos_men,
        'main_photos_women':main_photos_women,
        'parallax': parallax,
        'blogs_images': blogs_images,
        'insta_images': insta_images,

        'items': items,
    }
    
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def search(request):
    search = request.GET.get('search', "")

    if search:
        images = Image.objects.filter(variant__title__icontains=search).filter(is_main=True)
    else:
        images = []

    return render(request, 'search.html', {'images': images})


def faq(request):
    return render(request, 'faq.html')


def about_page(request):
    return render(request, 'about-page.html')


def error(request):
    return render(request, '404.html')