# Generated by Django 2.2.1 on 2019-05-14 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190514_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='description',
            new_name='name',
        ),
    ]