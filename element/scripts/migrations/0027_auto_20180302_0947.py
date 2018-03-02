# Generated by Django 2.0.1 on 2018-03-02 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0026_auto_20180302_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script_commonword',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
        migrations.AlterField(
            model_name='script_file',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
        migrations.AlterField(
            model_name='script_line',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
    ]
