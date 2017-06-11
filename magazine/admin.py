from django.contrib import admin
from magazine.models import Products, CategoryProducts, ManufacturesCategory, Manufactures, GalleryPhoto

class ProductsAdmin(admin.ModelAdmin):

    list_display = ('name_product', 'prise_product', 'category_product', 'active_product', 'rating_product', 'image_products')

    fieldsets = (
        (None, {
            'fields': ('name_product', 'code_product', 'prise_product', 'category_product', 'base_image_product')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('active_product', 'rating_product', 'slug_product'),
        }),
    )
    prepopulated_fields = {'slug_product': ('name_product',)}
    readonly_fields = ('rating_product',)

admin.site.register(Products, ProductsAdmin)

class CategoryProductsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug_category': ('name_category',)}
    list_display = ('name_category', 'parent_category', 'active_category', 'category_image')

admin.site.register(CategoryProducts, CategoryProductsAdmin)

admin.site.register(ManufacturesCategory)

admin.site.register(Manufactures)