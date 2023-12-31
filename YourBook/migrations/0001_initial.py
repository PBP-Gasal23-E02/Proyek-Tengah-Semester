# Generated by Django 4.2.6 on 2023-12-05 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PinjamBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petugas', models.TextField()),
                ('judul_buku', models.TextField()),
                ('durasi_pinjam', models.IntegerField()),
                ('catatan_peminjaman', models.TextField()),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.buku')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
