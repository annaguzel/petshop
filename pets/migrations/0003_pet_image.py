# Generated by Django 3.0.3 on 2020-02-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20200216_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]
