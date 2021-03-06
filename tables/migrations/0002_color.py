# Generated by Django 2.2.2 on 2020-03-07 15:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name_color', models.CharField(max_length=255)),
                ('code_color', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Colors',
                'ordering': ['name_color'],
            },
        ),
    ]
