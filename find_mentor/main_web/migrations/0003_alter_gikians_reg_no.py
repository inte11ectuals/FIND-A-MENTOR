# Generated by Django 4.0.4 on 2022-05-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0002_alter_gikians_id_alter_gikians_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gikians',
            name='reg_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
