# Generated by Django 2.0 on 2018-01-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahrefs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AhrefsBacklinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_from', models.CharField(blank=True, max_length=255, null=True)),
                ('url_to', models.CharField(blank=True, max_length=255, null=True)),
                ('ahrefs_rank', models.IntegerField(default=0, null=True)),
                ('domain_rating', models.IntegerField(default=0, null=True)),
                ('ip_from', models.CharField(blank=True, max_length=255, null=True)),
                ('links_internal', models.IntegerField(default=0, null=True)),
                ('links_external', models.IntegerField(default=0, null=True)),
                ('page_size', models.IntegerField(default=0, null=True)),
                ('encoding', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('first_seen', models.DateField(default=0, max_length=255, null=True)),
                ('last_visited', models.DateField(default=0, max_length=255, null=True)),
                ('prev_visited', models.DateField(default=0, max_length=255, null=True)),
                ('original', models.BooleanField(default=True)),
                ('link_type', models.CharField(blank=True, max_length=255, null=True)),
                ('redirect', models.IntegerField(default=0, null=True)),
                ('nofollow', models.BooleanField(default=True)),
                ('alt', models.CharField(blank=True, max_length=255, null=True)),
                ('anchor', models.CharField(blank=True, max_length=255, null=True)),
                ('text_pre', models.CharField(blank=True, max_length=255, null=True)),
                ('text_post', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
