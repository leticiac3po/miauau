# Generated by Django 3.1 on 2020-08-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gato_ou_cachorro', '0012_auto_20200818_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='prob',
            field=models.CharField(default='-1', max_length=20),
        ),
    ]
