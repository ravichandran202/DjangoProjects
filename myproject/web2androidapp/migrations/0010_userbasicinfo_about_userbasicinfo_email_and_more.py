# Generated by Django 4.1.7 on 2023-09-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web2androidapp", "0009_userbasicinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="userbasicinfo",
            name="about",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="first_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="phone",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="position",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userbasicinfo",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile"),
        ),
    ]
