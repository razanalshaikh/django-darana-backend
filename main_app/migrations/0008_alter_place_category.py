# Generated by Django 5.2 on 2025-05-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_place_categories_remove_place_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('NT', 'Nature'), ('CH', 'Culture & History'), ('SH', 'Shopping'), ('ET', 'Entertainment'), ('FB', 'Food & Beverages')], default='AD', max_length=2),
        ),
    ]
