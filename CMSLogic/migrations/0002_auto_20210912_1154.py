# Generated by Django 3.2.7 on 2021-09-12 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMSLogic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_Name', models.CharField(max_length=300)),
                ('Department_Head', models.CharField(max_length=300)),
                ('Department_ContactDetails', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='studentprofile',
            old_name='DateOfBirth',
            new_name='Date_Of_Birth',
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=50)),
                ('Event_Duration', models.DurationField()),
                ('Event_Head', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CMSLogic.studentprofile')),
            ],
        ),
    ]
