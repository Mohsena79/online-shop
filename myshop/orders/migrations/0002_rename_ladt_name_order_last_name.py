# Generated by Django 4.1.3 on 2022-12-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ladt_name',
            new_name='last_name',
        ),
    ]
