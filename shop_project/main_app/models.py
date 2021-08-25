from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория', unique=True)
    category_slug = models.SlugField(max_length=100, verbose_name='Слаг категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class CountryOfOrigin(models.Model):
    countryoforigin_name = models.CharField(max_length=100, verbose_name='Страна происхождения', unique=True)
    countryoforigin_slug = models.SlugField(max_length=100, verbose_name='Слаг страны происхождения')

    def __str__(self):
        return self.countryoforigin_name

    class Meta:
        verbose_name = 'Страна происхождения'
        verbose_name_plural = 'Страны происхождения'
        ordering =['countryoforigin_name']


class UnitOfMeasure(models.Model):
    unit_name = models.CharField(max_length=50, verbose_name='Единица измерения', unique=True)

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Наименование товара', unique=True)
    product_slug = models.SlugField(max_length=200, verbose_name='Слаг товара')
    product_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена товара', blank=True, null=True)
    product_quantity = models.PositiveIntegerField(verbose_name='Количество товара на складе', blank=True, null=True)
    product_units = models.ForeignKey('UnitOfMeasure', on_delete=models.CASCADE, verbose_name='Единицы измерения',
                                      blank=True, null=True)
    product_image = models.ImageField(verbose_name='Фото товара', upload_to='images/%Y/%M/%D', blank=True, null=True)
    is_available = models.BooleanField(default=True, verbose_name='Доступность', blank=True, null=True)
    product_countriesoforigin = models.ForeignKey('CountryOfOrigin', on_delete=models.CASCADE, verbose_name='Страны происхождения', blank=True, null=True)
    product_categories = models.ManyToManyField('Category', verbose_name='Категории', blank=True)
    product_description = models.TextField(verbose_name="Описание товара", blank=True, null=True)


    def __str__(self):
        return f'{self.product_name} ({self.product_countriesoforigin})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['product_name']
