# Generated by Django 4.2.6 on 2023-10-29 05:35

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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.IntegerField(blank=True, null=True)),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Issued', models.CharField(blank=True, max_length=255, null=True)),
                ('Title', models.CharField(blank=True, max_length=255, null=True)),
                ('Language', models.CharField(blank=True, max_length=255, null=True)),
                ('Authors', models.CharField(blank=True, max_length=255, null=True)),
                ('Subjects', models.CharField(blank=True, max_length=255, null=True)),
                ('LoCC', models.CharField(blank=True, max_length=255, null=True)),
                ('Bookshelves', models.CharField(default='Cookbooks and Cooking', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
