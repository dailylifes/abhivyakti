# Generated by Django 3.0.8 on 2020-12-21 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srmgpc', '0022_auto_20201221_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of performing event', max_length=100, null=True)),
                ('about', models.CharField(help_text='about the event', max_length=1000, null=True)),
                ('cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='srmgpc.CellName')),
            ],
        ),
    ]