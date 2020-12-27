# Generated by Django 3.1.3 on 2020-12-22 00:54

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('cabinspage', '0003_wagtailimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suitability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='suitability_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_suitability_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_services_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_room_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertySize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertysize_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_propertysize_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities_open_dates_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_opendates_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NearByWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='nearbywater_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_nearbywater_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NearbyCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='nearbycity_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_nearbycity_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities_general_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_general_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodDrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_drink_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_fooddrink_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_tags', to='wagtailcore.page')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinspage_activities_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]