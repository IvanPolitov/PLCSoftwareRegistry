# Generated by Django 4.2.5 on 2023-09-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', models.CharField(max_length=256)),
                ('creator', models.CharField(max_length=256)),
                ('crc_md5_user_software', models.CharField(max_length=256)),
                ('crc_md5_runtime', models.CharField(max_length=256)),
            ],
        ),
    ]