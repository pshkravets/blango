# Generated by Django 3.2.6 on 2024-04-04 11:43

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20240404_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(blank=True, default='0.5x0.5', editable=False, max_length=20, null=True),
        ),
    ]
