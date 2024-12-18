# Generated by Django 5.1.4 on 2024-12-18 13:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(db_default='Hello'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(default=datetime.datetime(2024, 12, 18, 18, 38, 25, 665778), on_delete=django.db.models.deletion.CASCADE, related_name='snippet', to='API.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(blank=True, db_default=datetime.datetime(2024, 12, 18, 18, 37, 42, 752242), default=datetime.datetime(2024, 12, 18, 18, 37, 42, 752242)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, db_default=datetime.datetime(2024, 12, 18, 18, 37, 42, 751257), default=datetime.datetime(2024, 12, 18, 18, 37, 42, 751257)),
        ),
    ]
