# Generated by Django 2.1.7 on 2019-05-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0004_endereco_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=80),
        ),
    ]
