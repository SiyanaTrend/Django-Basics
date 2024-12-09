# Generated by Django 5.1.4 on 2024-12-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('languages', models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('c', 'C'), ('cpp', 'C++'), ('other', 'Other')], default='other', max_length=20)),
            ],
        ),
    ]
