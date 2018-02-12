# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=500)),
                ('ordinal', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='IssueHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('creation_date', models.DateField()),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('repo_name', models.CharField(max_length=70)),
                ('owner_name', models.CharField(max_length=70)),
                ('type', models.CharField(choices=[('L', 'Local'), ('G', 'Git')], default='L', max_length=1)),
                ('url', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=40)),
                ('repository', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository')),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
            ],
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=4000)),
                ('repository', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='repository',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='repository',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='milestone',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository'),
        ),
        migrations.AddField(
            model_name='label',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository'),
        ),
        migrations.AddField(
            model_name='issuehistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ManyToManyField(related_name='issue_assignees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='history',
            field=models.ManyToManyField(to='igenapp.IssueHistory'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ManyToManyField(to='igenapp.Label'),
        ),
        migrations.AddField(
            model_name='issue',
            name='milestone',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='igenapp.Milestone'),
        ),
        migrations.AddField(
            model_name='issue',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository'),
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='igenapp.Issue'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='igenapp.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='wiki',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='igenapp.WikiPage'),
        ),
        migrations.AddField(
            model_name='activity',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igenapp.Repository'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
