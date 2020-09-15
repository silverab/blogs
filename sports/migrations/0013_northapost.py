# Generated by Django 2.2.7 on 2020-08-22 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sports', '0012_europepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='NorthAPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('size_1', models.ImageField(blank=True, null=True, upload_to='size_1/')),
                ('size_2', models.ImageField(blank=True, null=True, upload_to='size_2/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Category')),
            ],
            options={
                'ordering': ['-created'],
                'unique_together': {('title', 'slug')},
            },
        ),
    ]
