# Generated by Django 2.0 on 2018-10-28 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='Blog_type',
            new_name='blog_type',
        ),
    ]
