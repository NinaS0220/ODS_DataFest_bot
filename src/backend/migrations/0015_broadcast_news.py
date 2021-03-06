# Generated by Django 2.1.5 on 2019-05-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_tguser_on_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.TextField(choices=[('TEXT', 'TEXT'), ('IMAGE', 'IMAGE'), ('STICKER', 'STICKER'), ('LOCATION', 'LOCATION')], default='TEXT'),
        ),
        migrations.AddField(
            model_name='news',
            name='reporter_user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='target_group',
            field=models.TextField(choices=[('NONE', 'NONE'), ('NEWS_SUBSCRIPTION', 'NEWS_SUBSCRIPTION'), ('ADMINS', 'ADMINS'), ('WINNERS', 'WINNERS'), ('ALL', 'ALL')], default='NONE'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news',
            field=models.TextField(blank=True, default=''),
        ),
    ]
