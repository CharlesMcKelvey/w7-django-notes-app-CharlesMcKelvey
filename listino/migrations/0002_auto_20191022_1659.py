# Generated by Django 2.2.6 on 2019-10-22 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, help_text='Any information is okay to be given here.', null=True),
        ),
        migrations.CreateModel(
            name='NoteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='listino.Note')),
            ],
        ),
    ]
