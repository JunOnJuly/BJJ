# Generated by Django 3.2.12 on 2022-06-10 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.TextField(unique=True)),
                ('thumbnail', models.TextField()),
                ('description', models.TextField()),
                ('channel', models.TextField()),
                ('black', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videocomments', to='datas.video')),
            ],
        ),
    ]
