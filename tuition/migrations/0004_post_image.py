# Generated by Django 4.0.4 on 2022-04-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='tuition/images'),
        ),
    ]
