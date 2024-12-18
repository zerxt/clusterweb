# Generated by Django 5.1.3 on 2024-12-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('aspiration_message', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='information_center_photos/')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
