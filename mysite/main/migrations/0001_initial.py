# Generated by Django 4.2.3 on 2023-07-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JBNU',
            fields=[
                ('jid', models.IntegerField(primary_key=True, serialize=False)),
                ('jtitle', models.CharField(max_length=50)),
                ('jbelt', models.CharField(max_length=50)),
                ('jurl', models.CharField(max_length=50)),
                ('jdate', models.DateField()),
            ],
        ),
    ]