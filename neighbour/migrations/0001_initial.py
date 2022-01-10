# Generated by Django 3.2.10 on 2022-01-10 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('occupants', models.IntegerField(null=True)),
                ('police_dept', models.IntegerField(default='eg 999,269')),
                ('health_dept', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_photo', models.ImageField(null=True, upload_to='images/')),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('bio', models.CharField(default='Hi, I am using neighbourloop', max_length=150)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbour')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=130, null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='neighbour.neighbour')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=130, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbour')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
