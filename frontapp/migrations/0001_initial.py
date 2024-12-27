# Generated by Django 4.2.16 on 2024-12-05 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20, null=True)),
                ('pnumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('price', models.FloatField(null=True)),
                ('quantity', models.FloatField(null=True)),
                ('gst', models.IntegerField()),
                ('bill', models.FloatField(null=True)),
                ('preference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontapp.product')),
            ],
        ),
    ]
