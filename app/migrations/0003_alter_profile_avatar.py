# Generated by Django 4.1.4 on 2022-12-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/img/default-avatar-icon.jpg', null=True, upload_to=''),
        ),
    ]