# Generated by Django 4.1.7 on 2023-04-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile'),
        ),
    ]