# Generated by Django 4.1.7 on 2023-08-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_alter_comment_time_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.CharField(
                blank=True, default="11 August 2023", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.CharField(
                blank=True, default="11 August 2023", max_length=100
            ),
        ),
    ]