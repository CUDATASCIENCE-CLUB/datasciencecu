# Generated by Django 3.2.4 on 2021-06-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='images/Screenshot_20190819-232024_WhatsApp.JPG', null=True, upload_to='images/'),
        ),
    ]
