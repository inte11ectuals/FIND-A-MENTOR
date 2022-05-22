# Generated by Django 4.0.4 on 2022-05-21 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_web', '0012_alter_mentor_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gikians',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_web.university'),
        ),
        migrations.AlterField(
            model_name='mentees',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_web.gikians', to_field='year'),
        ),
    ]
