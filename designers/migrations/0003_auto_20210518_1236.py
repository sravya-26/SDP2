# Generated by Django 3.1.7 on 2021-05-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0002_designer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
        migrations.DeleteModel(
            name='Designer',
        ),
        migrations.DeleteModel(
            name='designers',
        ),
    ]
