# Generated by Django 5.1.3 on 2024-12-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcementTitle', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='announcements/')),
                ('writer', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
