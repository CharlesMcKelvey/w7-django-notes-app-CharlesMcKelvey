# Generated by Django 2.2.6 on 2019-10-23 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listino', '0002_auto_20191022_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noteitem',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='noteitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noteitem',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='noteitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
