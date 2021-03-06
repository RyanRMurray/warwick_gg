# Generated by Django 2.2 on 2019-05-01 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20180608_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.TextField()),
                ('status', models.CharField(choices=[('C', 'Complete'), ('R', 'Refunded'), ('P', 'In progress')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
