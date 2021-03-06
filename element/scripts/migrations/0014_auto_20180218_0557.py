# Generated by Django 2.0.1 on 2018-02-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0013_line_sentences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script_Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Line')),
            ],
        ),
        migrations.RemoveField(
            model_name='script',
            name='lines',
        ),
        migrations.AddField(
            model_name='script_line',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.Script'),
        ),
        migrations.AddField(
            model_name='script',
            name='lines2',
            field=models.ManyToManyField(blank=True, through='scripts.Script_Line', to='scripts.Line'),
        ),
    ]
