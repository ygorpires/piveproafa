# Generated by Django 2.1.7 on 2019-05-01 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20190501_1543'),
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]