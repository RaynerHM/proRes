# Generated by Django 2.0 on 2018-05-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Residencial', '0011_auto_20180503_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajuste',
            name='fecha_Limite_Pago',
            field=models.DateField(verbose_name='Fecha Limite De Pago'),
        ),
        migrations.AlterField(
            model_name='ajuste',
            name='fecha_Para_Facturar',
            field=models.DateField(verbose_name='Fecha Para Facturar'),
        ),
    ]