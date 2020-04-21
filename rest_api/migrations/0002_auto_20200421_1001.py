# Generated by Django 3.0.2 on 2020-04-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_status',
            field=models.CharField(blank=True, choices=[('n', 'None'), ('nc', 'Needs Content'), ('nr', 'Needs Review'), ('a', 'Approved')], default='n', help_text='Article status', max_length=2),
        ),
    ]
