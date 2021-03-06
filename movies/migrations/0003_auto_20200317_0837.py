# Generated by Django 3.0.4 on 2020-03-17 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200317_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mpa_rating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], default='R', max_length=10),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='torrents',
        ),
        migrations.AddField(
            model_name='movie',
            name='torrents',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.Torrent'),
        ),
    ]
