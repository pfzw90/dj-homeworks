# Generated by Django 3.1.2 on 2021-02-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_measurement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='uploaded_images/'),
        ),
    ]