# Generated by Django 2.1.2 on 2019-05-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190514_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_category',
            field=models.CharField(choices=[('C언어', 'C언어'), ('Django', 'Django'), ('Front-End', 'Front-End'), ('IT', 'IT'), ('시사', '시사')], default='IT', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Projects', 'Projects'), ('Study', 'Study'), ('Article', 'Article')], default='Study', max_length=20),
        ),
    ]
