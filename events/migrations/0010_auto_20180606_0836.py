# Generated by Django 2.0.2 on 2018-06-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_eventsignup_transaction_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsignup',
            name='is_unsigned_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventsignup',
            name='refund_token',
            field=models.TextField(blank=True),
        ),
    ]
