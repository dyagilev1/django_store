# Generated by Django 4.2.1 on 2023-05-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_brand_options_rename_name_brand_brand_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]