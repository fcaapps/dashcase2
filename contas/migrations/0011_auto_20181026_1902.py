# Generated by Django 2.1.2 on 2018-10-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0010_auto_20181026_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='custom_email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Usuário / E-mail'),
        ),
    ]