# Generated by Django 3.2.9 on 2021-11-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
    ]
