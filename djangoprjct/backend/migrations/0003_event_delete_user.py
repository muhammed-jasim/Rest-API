# Generated by Django 4.2.6 on 2023-10-31 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_date', models.DateField(auto_now_add=True)),
                ('evnt_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
