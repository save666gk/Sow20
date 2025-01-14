# Generated by Django 5.0.4 on 2024-05-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sownh', '0002_categorynews_alter_category_options_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя тега')),
            ],
        ),
        migrations.AlterModelOptions(
            name='categorynews',
            options={'verbose_name': 'Категории_Новости', 'verbose_name_plural': 'Категории_Новости'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Фото проекта'),
        ),
        migrations.CreateModel(
            name='CaseCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название работы')),
                ('image', models.ImageField(upload_to='case_images/', verbose_name='Изображение')),
                ('client_business_task', models.TextField(verbose_name='Бизнес задача клиента')),
                ('view_link', models.URLField(verbose_name='Ссылка на кейс')),
                ('category_tags', models.ManyToManyField(related_name='case_cards', to='sownh.categorytag', verbose_name='Категории')),
            ],
        ),
    ]
