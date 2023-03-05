# Generated by Django 4.1.7 on 2023-03-04 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(db_index=True, max_length=32)),
                ('call_duration', models.IntegerField()),
            ],
            options={
                'db_table': 'calls',
            },
        ),
    ]