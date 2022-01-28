# Generated by Django 4.0.1 on 2022-01-28 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('height', models.CharField(blank=True, max_length=5, null=True)),
                ('race', models.CharField(max_length=100)),
                ('birth', models.CharField(max_length=100)),
                ('death', models.CharField(max_length=100)),
                ('realm', models.CharField(max_length=100)),
                ('hair', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('wikiUrl', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
    ]
