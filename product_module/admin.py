from django.contrib import admin
from .models import CartItem

from  .models import *

# Register your models here.
admin.site.register(Brand)
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
 list_display = ["image_tag", "name", "price", "brand", "category",]
 search_fields = ["name", "price", "brand__name", "category__name",]
 list_filter = ["brand","category",]
#  readonly_fields = ["quantity",]
 
class Meta:
    model = Product
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

admin.site.register(CartItem)






