# Generated by Django 4.1.7 on 2023-04-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(default='profile.jpg', upload_to='Profile'),
        ),
    ]
