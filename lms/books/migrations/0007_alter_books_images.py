# Generated by Django 4.2.7 on 2023-11-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_books_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='images',
            field=models.ImageField(null=True, upload_to='books/images'),
        ),
    ]