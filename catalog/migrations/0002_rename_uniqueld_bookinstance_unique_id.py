# Generated by Django 4.2.2 on 2023-06-08 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='uniqueld',
            new_name='unique_id',
        ),
    ]