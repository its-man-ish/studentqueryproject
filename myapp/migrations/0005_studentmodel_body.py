# Generated by Django 3.1.4 on 2021-02-15 15:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_studentmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
