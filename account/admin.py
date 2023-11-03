from django.contrib import admin
from .models import *

# Register your models here.

class WishListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_id', 'username', 'product_photo']
    list_display_links = ['title', 'product_photo']
    search_fields = ['title']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['get_title', 'user_id', 'username', 'title', 'text', 'product_photo']
    list_display_links = ['get_title', 'product_photo']
    readonly_fields = ['title', 'text']
    search_fields = ['title', 'text']

admin.site.register(User)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Vendor)
admin.site.register(Cart)
admin.site.register(Review, ReviewAdmin)