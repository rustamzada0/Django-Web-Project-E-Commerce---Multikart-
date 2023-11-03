from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from core.models import MainPhotos
from django.views.generic.base import TemplateView
from .models import *
from account.models import *
from .forms import ReviewForm

# Create your views here.

# class CategoryPage(TemplateView):

#     template_name = 'category-page.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         categories = Category.objects.all()

#         for category in categories:
#             if category.get_absolute_url() == f"{self.kwargs.get('path')}":
#                 category = category
#                 break

#         images = Image.objects.filter(is_main=True)
#         variant = Variant.objects.all()

#         menu = MainPhotos.objects.get(id=6)
                
#         context['category'] = category
#         context['images'] = images
#         context['variant'] = variant
#         context['menu'] = menu

#         return context


def category_page(request):
    # categories = Category.objects.filter(slug = path.split('/')[-1])
    # for category in categories:
    #     if category.get_absolute_url() == f"{path}":
    #         category = category
    #         break
    
    # if category.parent:
    #     items = Image.objects.filter(variant__product__category = category).filter(variant__is_main_variant=True).filter(is_main=True)
    # else:
    #     child_categories1 = []
    #     cats = Category.objects.all()
    #     for cat in cats:
    #         if cat.parent:
    #             if category.title == cat.title:
    #                 child_categories1.append(cat)
    #     child_categories2 = Category.objects.filter(parent=category)

    #     items_list = []
    #     items = []

    #     for cat in child_categories1:
    #         items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))
    #     for cat in child_categories2:
    #         items_list.append(Image.objects.filter(variant__product__category = cat).filter(variant__is_main_variant=True).filter(is_main=True))
    #     for item_list in items_list:
    #         for item in item_list:
    #             items.append(item)

    colors = Color.objects.all()
    menu = MainPhotos.objects.get(id=6)

    context = {
        # 'items': items,
        'menu': menu,
        'colors': colors
    }

    return render(request , "category-page.html", context)


def product_page(request, path, slug):
    # Product
    variant = get_object_or_404(Variant, slug=slug)
    if not variant.get_absolute_url() == f"{path}/{slug}":
        raise Http404
    images = Image.objects.filter(variant=variant).all()
    # End Product

    # Wishlist
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user)
        variants = []
        for wish in wishlist:
            variants.append(wish.variant) # wishlistdeki variantlar | html-da if variant in variants 
    else:
        if request.session.get("wishlist"):
            variants = request.session["wishlist"].split()
            variants = [int(i) for i in variants]
        else:
            variants = []
    # End Wishlist

    # Review
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.variant = variant
            review.save()
    else:
        form = ReviewForm()
    # End Review

    # Related Products
    is_main_variant = Variant.objects.filter(product=variant.product).filter(is_main_variant=True).first()
    item_ = Image.objects.filter(variant=is_main_variant).first()
    related_items = Image.objects.filter(variant__is_main_variant=True).filter(variant__product__category = variant.product.category).filter(is_main=True)
    # End Related Products

    product_variant_list = Variant.objects.filter(product=variant.product)

    context = {
        'variant': variant,
        'images': images,
        'variants': variants,
        'related_items': related_items,
        'item_': item_,
        'product_variant_list': product_variant_list,
        'form': form
    }
    return render(request, 'product-page.html', context)