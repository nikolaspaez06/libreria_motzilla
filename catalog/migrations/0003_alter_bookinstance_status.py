# Generated by Django 4.2.2 on 2023-06-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_uniqueld_bookinstance_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('mat', 'Maintenance'), ('ol', 'On loan'), ('avi', 'Available'), ('rev', 'Reserved')], default='mat', help_text='Book availability', max_length=4),
        ),
    ]
