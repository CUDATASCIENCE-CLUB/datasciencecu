# Generated by Django 3.2.4 on 2021-06-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_thread_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
