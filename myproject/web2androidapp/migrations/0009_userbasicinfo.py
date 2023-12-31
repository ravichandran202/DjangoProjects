# Generated by Django 4.1.7 on 2023-09-03 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("web2androidapp", "0008_appdetails_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserBasicInfo",
            fields=[
                (
                    "basicinfo_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web2androidapp.basicinfo",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("web2androidapp.basicinfo",),
        ),
    ]
