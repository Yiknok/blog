# Generated by Django 4.1.1 on 2022-09-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Category URL')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tag Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Tag URL')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Post Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Post URL')),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='Post Author')),
                ('content', models.TextField(blank=True, verbose_name='Post Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created:')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Post Image')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category', verbose_name='Post Category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.tag', verbose_name='Post Tags')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
