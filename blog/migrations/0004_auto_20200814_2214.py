# Generated by Django 2.2.10 on 2020-08-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pubdate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='發佈時間'),
        ),
    ]