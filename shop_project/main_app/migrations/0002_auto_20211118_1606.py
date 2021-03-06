# Generated by Django 3.2.8 on 2021-11-18 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='countryoforigin',
            options={'ordering': ['countryoforigin_name'], 'verbose_name': 'Страна происхождения', 'verbose_name_plural': 'Страны происхождения'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='unitofmeasure',
            options={'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_categories',
            field=models.ManyToManyField(blank=True, to='main_app.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.unitofmeasure', verbose_name='Единицы измерения'),
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product', verbose_name='Наименование продукта')),
            ],
        ),
    ]
