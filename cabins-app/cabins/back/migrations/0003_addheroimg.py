# Generated by Django 3.1.3 on 2020-12-20 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('cabinsback', '0002_wagtailimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
