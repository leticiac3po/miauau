# Generated by Django 3.1 on 2020-08-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gato_ou_cachorro', '0011_auto_20200817_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imagem',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='lbl',
            field=models.CharField(default='error', max_length=20),
        ),
    ]