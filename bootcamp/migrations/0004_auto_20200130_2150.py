# Generated by Django 3.0.2 on 2020-01-30 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0003_auto_20200130_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='bootcamp.Instructor'),
        ),
    ]
