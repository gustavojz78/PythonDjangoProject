# Generated by Django 4.1.2 on 2022-11-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0014_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(max_length=5000),
        ),
    ]
