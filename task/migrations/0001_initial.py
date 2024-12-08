# Generated by Django 5.1.3 on 2024-12-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_Title', models.CharField(max_length=80)),
                ('Completed', models.BooleanField(default=False)),
                ('Creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
