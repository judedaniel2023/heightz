# Generated by Django 5.0.4 on 2024-04-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user_image',
            field=models.ImageField(default='images.png', upload_to='uploads/testimonial/'),
        ),
    ]
