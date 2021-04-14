# Generated by Django 3.1.7 on 2021-04-12 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGranulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchno', models.CharField(max_length=10)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.product')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Main.room')),
            ],
        ),
    ]