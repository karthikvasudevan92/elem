# Generated by Django 2.0.1 on 2018-02-14 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0007_auto_20180213_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagged',
            name='script',
        ),
        migrations.RemoveField(
            model_name='tagged',
            name='tag',
        ),
        migrations.AlterField(
            model_name='line',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
        migrations.DeleteModel(
            name='Tagged',
        ),
    ]
