# Generated by Django 3.0.2 on 2020-01-30 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0002_auto_20200130_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='instructor',
        ),
    ]
