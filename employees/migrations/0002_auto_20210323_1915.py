# Generated by Django 3.1.7 on 2021-03-23 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='leave_data',
            new_name='leave_date',
        ),
    ]
