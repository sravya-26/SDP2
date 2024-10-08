# Generated by Django 3.1.7 on 2021-05-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0003_auto_20210518_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('mensfashion', 'Mensfashion'), ('womensfashion', 'Womensfashion')], default='mensfashion', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='price',
            field=models.FloatField(),
        ),
    ]
