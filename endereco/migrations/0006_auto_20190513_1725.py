# Generated by Django 2.1.7 on 2019-05-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0005_auto_20190513_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
