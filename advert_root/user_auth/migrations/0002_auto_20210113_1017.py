# Generated by Django 3.1.5 on 2021-01-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Per', 'Personal'), ('Pro', 'Professional'), ('Ent', 'Enterprise'), ('PME', 'Small Business'), ('Bus', 'Business'), ('Org', 'Organization'), ('Mag', 'Magazine')], default='Per', max_length=50),
        ),
    ]
