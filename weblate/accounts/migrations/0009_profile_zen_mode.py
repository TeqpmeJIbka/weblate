# Generated by Django 2.2 on 2019-05-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190426_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='zen_mode',
            field=models.IntegerField(choices=[(0, 'Vertical'), (1, 'Horizontal')], default=0, verbose_name='Zen editor mode'),
        ),
    ]
