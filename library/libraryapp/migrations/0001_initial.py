# Generated by Django 4.0.4 on 2022-06-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('issued_date', models.DateField()),
                ('submitted_date', models.DateField()),
            ],
        ),
    ]
