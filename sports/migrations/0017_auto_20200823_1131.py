# Generated by Django 2.2.7 on 2020-08-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0016_auto_20200823_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='africapost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='asiapost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='centerpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='europepost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='leftpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minicenterpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='northamericapost',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rightpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
