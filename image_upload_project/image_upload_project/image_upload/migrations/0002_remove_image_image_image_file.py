# Generated by Django 5.1 on 2024-08-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.FileField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
