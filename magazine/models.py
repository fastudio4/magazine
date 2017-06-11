from django.db import models
from ckeditor.fields import RichTextField


class Products(models.Model):
    class Meta:
        db_table = 'products'
    name_product = models.CharField(verbose_name='Name product', max_length=200)
    code_product = models.CharField(verbose_name='Code product', max_length=100)
    prise_product = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Prise product')
    slug_product = models.SlugField(
        max_length=100,
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
    )
    base_image_product = models.ImageField(
        verbose_name='Base image',
        upload_to='images/product_image',
        blank=True,
        null=True,
        default=None,
    )

    description_product = RichTextField(config_name='back', verbose_name='Description product')
    category_product = models.ForeignKey('CategoryProducts', verbose_name='Category product')
    manufactures_product = models.ForeignKey('Manufactures')
    title_product_seo = models.CharField(verbose_name='Title SEO', max_length=150)
    description_seo = models.TextField(verbose_name='SEO description')
    keywords_seo = models.TextField(verbose_name='SEO keywords')
    active_product = models.BooleanField(verbose_name='Active product', default=True)
    rating_product = models.PositiveIntegerField(verbose_name='Rating product', default=0)

    def image_products(self):
        if self.base_image_product:
            return '<b style="color: green;">IMAGE</b>'
        else:
            return '<b style="color: red;">NO IMAGE</b>'
    image_products.allow_tags = True

    def __str__(self):
        return self.name_product

class GalleryPhoto(models.Model):
    class Meta:
        db_table = 'gallery_image'
    gallery_image = models.ImageField(
        verbose_name='Gallery image',
        upload_to='images/gallery_image',
        blank=True,
        null=True,
        default=None,
    )
    product = models.ForeignKey('Products')


class CategoryProducts(models.Model):
    class Meta:
        db_table = 'category'
    name_category = models.CharField(max_length=100, verbose_name='Name category')
    parent_category = models.ForeignKey(
        'CategoryProducts',
        blank=True,
        null=True,
        default=None
    )
    slug_category = models.SlugField(
        max_length=100,
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
    )
    title_category_seo = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None
    )
    image_category = models.ImageField(
        verbose_name='Image category',
        upload_to='images/category_images',
        blank=True,
        null=True,
        default=None,
    )
    description_category = RichTextField(config_name='back', verbose_name='Description category')
    active_category = models.BooleanField(default=True, verbose_name='Active category')
    keywords_category_seo = models.TextField(verbose_name='Keywords seo site')
    description_category_seo = models.TextField(verbose_name='Description seo site')

    def category_image(self):
        if self.image_category:
            return '<b style="color: green;">IMAGE</b>'
        else:
            return '<b style="color: red;">NO IMAGE</b>'
    category_image.allow_tags = True

    def __str__(self):
        return self.name_category


class ManufacturesCategory(models.Model):
    class Meta:
        db_table = 'man_category'
    name_cat_manufactures = models.CharField(verbose_name='Category manufactures', max_length=50)

    def __str__(self):
        return self.name_cat_manufactures

class Manufactures(models.Model):
    class Meta:
        db_table = 'manufactures'
    name_manufactures = models.CharField(
        verbose_name='Name manufactures',
        max_length=150
    )
    category_manufactures = models.ManyToManyField(
        'ManufacturesCategory',
        verbose_name='Category manufactures'
    )
    slug_manufactures = models.SlugField(
        max_length=100,
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
    )
    site_manufacturas = models.URLField(
        verbose_name='URL Manufactures',
        blank=True,
        null=True,
        default=None,
    )
    logo_manufactures = models.ImageField(
        verbose_name='Logo manufactures',
        upload_to='images/manufactures_logo',
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.name_manufactures