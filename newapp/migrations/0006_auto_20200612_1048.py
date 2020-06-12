# Generated by Django 3.0.6 on 2020-06-12 07:48

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20200612_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgpagetag',
            name='img_content_object',
        ),
        migrations.AddField(
            model_name='imgpagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='newapp.ImgPage'),
            preserve_default=False,
        ),
    ]
