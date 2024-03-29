# Generated by Django 4.1.2 on 2023-02-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eventteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('et_name', models.CharField(max_length=50)),
                ('et_insta', models.URLField(default='some_value')),
                ('et_linkedin', models.URLField(default='some_value')),
                ('et_teamname', models.CharField(max_length=50)),
                ('et_image', models.FileField(default=None, max_length=250, null=True, upload_to='')),
                ('et_shortdesc', models.TextField()),
            ],
        ),
    ]
