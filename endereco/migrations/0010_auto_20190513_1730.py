# Generated by Django 2.1.7 on 2019-05-13 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0009_auto_20190513_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cliente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]
