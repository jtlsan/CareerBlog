# Generated by Django 2.1.2 on 2019-05-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devnews',
            name='category',
            field=models.CharField(choices=[('Projects', 'Projects'), ('Study', 'Study'), ('외부컨텐츠', '외부컨텐츠')], default='Study', max_length=10),
        ),
    ]
