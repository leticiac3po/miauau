# Generated by Django 3.1 on 2020-08-13 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gato_ou_cachorro', '0003_auto_20200813_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img',
            new_name='imagem',
        ),
    ]