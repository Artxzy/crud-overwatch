# Generated by Django 2.2.1 on 2019-05-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20190504_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroi',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='afiliacao',
            field=models.CharField(max_length=100, verbose_name='Afiliação'),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='historia',
            field=models.TextField(max_length=10000, verbose_name='História'),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='nome_verdadeiro',
            field=models.CharField(max_length=100, verbose_name='Nome verdadeiro; idade'),
        ),
        migrations.AlterField(
            model_name='heroi',
            name='ocupacao',
            field=models.CharField(max_length=100, verbose_name='Ocupação'),
        ),
    ]
