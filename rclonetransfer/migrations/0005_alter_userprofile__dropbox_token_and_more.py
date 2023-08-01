# Generated by Django 4.2.3 on 2023-08-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rclonetransfer', '0004_alter_userprofile_dropbox_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='_dropbox_token',
            field=models.JSONField(blank=True, db_column='dropbox_token', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='_google_token',
            field=models.JSONField(blank=True, db_column='google_token', null=True),
        ),
    ]