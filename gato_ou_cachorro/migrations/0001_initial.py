# Generated by Django 3.1 on 2020-08-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='imgs/no-img.jpg', upload_to='imgs/')),
                ('lbl', models.CharField(default='não classificada', max_length=200)),
            ],
        ),
    ]