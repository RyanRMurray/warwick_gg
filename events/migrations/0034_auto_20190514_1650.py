# Generated by Django 2.2.1 on 2019-05-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0033_auto_20190506_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsignup',
            name='comment',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
