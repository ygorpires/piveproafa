# Generated by Django 2.1.7 on 2019-05-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0003_remove_endereco_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
