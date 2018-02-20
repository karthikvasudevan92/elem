# Generated by Django 2.0.1 on 2018-02-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0014_auto_20180218_0557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='lines2',
            new_name='lines',
        ),
        migrations.AlterField(
            model_name='script_line',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
    ]
