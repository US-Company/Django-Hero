# Generated by Django 3.0.8 on 2020-07-18 00:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_table_background_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
