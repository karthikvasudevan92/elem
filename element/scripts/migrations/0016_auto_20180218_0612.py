# Generated by Django 2.0.1 on 2018-02-18 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0015_auto_20180218_0557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='script_line',
            options={'ordering': ('line',)},
        ),
        migrations.AlterField(
            model_name='script_line',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
    ]
