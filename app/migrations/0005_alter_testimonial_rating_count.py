# Generated by Django 5.0.4 on 2024-04-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_testimonial_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating_count',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
