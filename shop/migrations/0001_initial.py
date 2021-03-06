# Generated by Django 3.0.8 on 2020-09-26 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubric_name', models.CharField(db_index=True, max_length=20, verbose_name='Rubric Name')),
            ],
            options={
                'verbose_name': 'Rubric',
                'verbose_name_plural': 'Rubrics',
                'ordering': ['rubric_name'],
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('short_description', models.TextField(default='SOME Short Description', verbose_name='Short Description')),
                ('long_description', models.TextField(default='SOME Long Description', verbose_name='Long Description')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Rubric', verbose_name='Rubric')),
            ],
            options={
                'verbose_name': 'Seed',
                'verbose_name_plural': 'Seeds',
            },
        ),
    ]
