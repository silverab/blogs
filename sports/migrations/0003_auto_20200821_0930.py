# Generated by Django 2.2.7 on 2020-08-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20200821_0755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='size_1',
            field=models.ImageField(blank=True, null=True, upload_to='size_1/'),
        ),
        migrations.AddField(
            model_name='post',
            name='size_2',
            field=models.ImageField(blank=True, null=True, upload_to='size_2/'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'slug')},
        ),
        migrations.RemoveField(
            model_name='post',
            name='blog_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='feature_image',
        ),
    ]
