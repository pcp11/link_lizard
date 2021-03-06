# Generated by Django 3.0.5 on 2020-06-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('generated_hash', models.TextField()),
                ('created', models.DateTimeField(editable=False)),
            ],
        ),
    ]
