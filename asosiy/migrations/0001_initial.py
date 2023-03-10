# Generated by Django 4.1.7 on 2023-02-20 12:37

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
            name='Ombor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=13)),
                ('ism', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('brend', models.CharField(max_length=50)),
                ('narx', models.IntegerField()),
                ('kelgan_sana', models.DateField()),
                ('miqdor', models.IntegerField()),
                ('olchov', models.CharField(max_length=50)),
                ('omborfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.ombor')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=55)),
                ('nom', models.CharField(max_length=40)),
                ('manzil', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=13)),
                ('qarz', models.IntegerField()),
                ('omborfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.ombor')),
            ],
        ),
    ]
