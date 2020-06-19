# Generated by Django 3.0.6 on 2020-06-12 07:26

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('newapp', '0003_auto_20200601_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Text to describe the page')),
                ('image', wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))], blank=True, verbose_name='Image')),
                ('date_published', models.DateField(blank=True, null=True, verbose_name='Date page published')),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='newapp.AppCategory')),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='newapp.AppPageTag', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]