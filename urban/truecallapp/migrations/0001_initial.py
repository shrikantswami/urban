# Generated by Django 2.0.7 on 2018-08-31 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='true_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('platform', models.CharField(choices=[('Andriod', 'Andriod'), ('IPhone', 'iPhone'), ('truecaller_business', 'Truecaller_business'), ('Developer_l', 'developer')], max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('subject', models.CharField(max_length=30)),
                ('attachment', models.FileField(upload_to='')),
                ('region', models.CharField(choices=[('eu', 'eu__eea_and_switzerland'), ('World', 'rest_of_the_world')], max_length=10)),
            ],
        ),
    ]
