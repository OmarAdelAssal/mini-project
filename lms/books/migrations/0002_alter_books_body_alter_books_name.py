# Generated by Django 4.2.7 on 2023-11-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='body',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
