# Generated by Django 2.0.7 on 2018-09-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecallapp', '0002_auto_20180901_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='true_form',
            old_name='attachment',
            new_name='Attachment',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='platform',
            new_name='Platform',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='region',
            new_name='Region',
        ),
        migrations.RenameField(
            model_name='true_form',
            old_name='subject',
            new_name='Subject',
        ),
        migrations.AddField(
            model_name='true_form',
            name='Cover_Later',
            field=models.ImageField(blank=True, upload_to='cover_Later'),
        ),
    ]