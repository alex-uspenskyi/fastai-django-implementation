# Generated by Django 2.1.5 on 2019-02-03 15:28

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField(verbose_name='datePublished')),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
