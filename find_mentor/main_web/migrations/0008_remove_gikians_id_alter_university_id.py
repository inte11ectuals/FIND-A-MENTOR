# Generated by Django 4.0.4 on 2022-05-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0007_alter_gikians_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gikians',
            name='id',
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
