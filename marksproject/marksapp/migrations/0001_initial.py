# Generated by Django 3.1.2 on 2021-06-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Section', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Marks_obtained', models.IntegerField()),
            ],
        ),
    ]
