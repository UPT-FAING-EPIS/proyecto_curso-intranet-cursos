# Generated by Django 4.2 on 2023-04-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbCreditos',
            fields=[
                ('CodCredito', models.AutoField(primary_key=True, serialize=False)),
                ('TipCredito', models.CharField(max_length=50)),
            ],
        ),
    ]
